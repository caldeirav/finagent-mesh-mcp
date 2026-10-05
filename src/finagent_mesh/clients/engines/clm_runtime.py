"""Architecture-true CLM-8B without the contrastive-lm/vLLM extra.

Contrastive-LM/CLM-v0.1-8B on Hugging Face is the ~75MB projection heads, not a
standalone 8B net. Official inference (Apache-2.0 CLM paper/repo):

  encoder: Qwen/Qwen3-8B, last-token pooling, 2048 tokens, 4096-d
  heads:   CLM_v0.1-8B.pt (state_head + action_head + logit_scale)
  score:   exp(logit_scale) * cos(state_head(s), action_head(c)) then softmax

We do not import `contrastive-lm` (it depends on vLLM and cannot lock against
torch>=2.14 / transformers>=5). Optional CLM_EMB_URL still uses a pooling server
if one is already running.
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Any

from finagent_mesh.runtime.progress import log

CLM_ENCODER_DEFAULT = "Qwen/Qwen3-8B"
HF_REPO = "Contrastive-LM/CLM-v0.1-8B"
HF_FILE = "CLM_v0.1-8B.pt"
HIDDEN = 4096
PROJ_DIM = 512
CLM_INSTALL_HINT = (
    "CLM-8B needs `uv sync --extra real` (torch, transformers, huggingface-hub) "
    "and will download Qwen/Qwen3-8B plus Contrastive-LM/CLM-v0.1-8B heads. "
    "Decision-2.0 Kai is not a CLM substitute."
)


class Qwen3LastTokenEmbedder:
    """Last-token pooled Qwen3-8B embeddings, L2-normalised (n, 4096)."""

    def __init__(self, model_id: str | None = None) -> None:
        self.model_id = model_id or os.getenv("CLM_ENCODER_ID", CLM_ENCODER_DEFAULT)
        self.max_tokens = int(os.getenv("CLM_MAX_TOKENS", "2048"))
        self.batch = int(os.getenv("CLM_EMBED_BATCH", "8"))

    def embed(self, texts: list[str]) -> tuple[Any, int]:
        import numpy as np
        import torch

        from finagent_mesh.clients.engines.real_infer import RealInferError, _load_embedder

        tok, model, device = _load_embedder(self.model_id)
        tok.padding_side = "left"
        if tok.pad_token_id is None and tok.eos_token_id is not None:
            tok.pad_token = tok.eos_token
        chunks: list[Any] = []
        tokens = 0
        for i in range(0, len(texts), self.batch):
            batch = texts[i : i + self.batch]
            enc = tok(
                batch,
                padding=True,
                truncation=True,
                max_length=self.max_tokens,
                return_tensors="pt",
            )
            tokens += int(enc["attention_mask"].sum().item())
            enc = {k: v.to(device) for k, v in enc.items()}
            with torch.no_grad():
                out = model(**enc)
                hidden = getattr(out, "last_hidden_state", None)
                if hidden is None:
                    raise RealInferError(
                        f"CLM encoder {self.model_id} produced no last_hidden_state"
                    )
                vec = hidden[:, -1, :].float()
                vec = torch.nn.functional.normalize(vec, p=2, dim=1)
            chunks.append(vec.cpu().numpy())
        return np.concatenate(chunks, axis=0), tokens


def download_clm_heads() -> str:
    dest_dir = os.environ.get(
        "CLM_CKPT_DIR", os.path.join(os.path.expanduser("~"), ".cache", "clm")
    )
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, HF_FILE)
    env_ckpt = os.getenv("CLM_CKPT")
    if env_ckpt and os.path.exists(env_ckpt):
        return env_ckpt
    if os.path.exists(dest):
        return dest
    from huggingface_hub import hf_hub_download

    from finagent_mesh.clients.engines.hf_auth import ensure_hf_hub_auth

    token = ensure_hf_hub_auth()
    log(f"Downloading CLM heads {HF_REPO}/{HF_FILE}…")
    return hf_hub_download(HF_REPO, HF_FILE, local_dir=dest_dir, token=token)


def _make_head(*, width: int, depth: int, proj: int, activation: str, layernorm: bool, residual: bool, hidden: int):
    import torch.nn as nn

    act_cls = {"gelu": nn.GELU, "relu": nn.ReLU, "silu": nn.SiLU}[activation]

    class Head(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.inp = nn.Linear(hidden, width)
            self.hidden = nn.ModuleList(nn.Linear(width, width) for _ in range(max(depth - 2, 0)))
            self.norms = nn.ModuleList(
                (nn.LayerNorm(width) if layernorm else nn.Identity()) for _ in range(max(depth - 2, 0))
            )
            self.out = nn.Linear(width, proj)
            self.act = act_cls()
            self.residual = residual

        def forward(self, x):
            x = self.act(self.inp(x))
            for lin, nrm in zip(self.hidden, self.norms):
                h = self.act(nrm(lin(x)))
                x = x + h if self.residual else h
            return self.out(x)

    return Head()


class ClmHeadPair:
    def __init__(self, path: str, device: str) -> None:
        import torch

        ck = torch.load(path, map_location="cpu", weights_only=False)
        cfg = dict(ck["cfg"])
        kw = dict(
            width=cfg["width"],
            depth=cfg["depth"],
            proj=ck.get("projection_dim", cfg.get("projection_dim", PROJ_DIM)),
            activation=cfg.get("activation", "gelu"),
            layernorm=cfg.get("layernorm", False),
            residual=cfg.get("residual", False),
            hidden=cfg.get("hidden_size", HIDDEN),
        )
        sh, ah = _make_head(**kw), _make_head(**kw)
        sh.load_state_dict(ck["state_head"])
        ah.load_state_dict(ck["action_head"])
        self.state_head = sh.eval().to(device)
        self.action_head = ah.eval().to(device)
        self.device = device
        self.scale = float(torch.as_tensor(ck["logit_scale"]).float().exp().clamp(max=100.0))

    def _project(self, head, x):
        import torch

        with torch.no_grad():
            t = torch.from_numpy(x).to(self.device)
            return torch.nn.functional.normalize(head(t), dim=-1)

    def project_states(self, states):
        return self._project(self.state_head, states)

    def project_actions(self, candidates):
        return self._project(self.action_head, candidates)


class LocalClmEngine:
    def __init__(self, embedder: Qwen3LastTokenEmbedder, heads: ClmHeadPair) -> None:
        self.embedder = embedder
        self.heads = heads

    def rank(
        self,
        state: str,
        candidates: list[str],
        instructions: str | None = None,
    ) -> list[dict[str, Any]]:
        import torch

        ins = (instructions or "").strip()
        state_text = f"{state.strip()}\n\n{ins}" if ins else state.strip()
        texts = [state_text] + list(candidates)
        emb, _spent = self.embedder.embed(texts)
        zq = self.heads.project_states(emb[:1])
        za = self.heads.project_actions(emb[1:])
        logits = (self.heads.scale * (za @ zq[0])).float()
        probs = torch.softmax(logits, dim=0).cpu().tolist()
        order = sorted(range(len(candidates)), key=lambda i: -probs[i])
        return [
            {"rank": r + 1, "candidate": candidates[i], "prob": float(probs[i])}
            for r, i in enumerate(order)
        ]


@lru_cache(maxsize=1)
def load_clm_engine(encoder_id: str = CLM_ENCODER_DEFAULT) -> LocalClmEngine:
    from finagent_mesh.clients.engines.real_infer import _torch_device

    device = str(_torch_device())
    log(
        f"CLM encoder: in-process last-token pooling {encoder_id} on {device}; "
        f"heads={HF_REPO}/{HF_FILE}"
    )
    path = download_clm_heads()
    heads = ClmHeadPair(path, device)
    return LocalClmEngine(Qwen3LastTokenEmbedder(encoder_id), heads)
