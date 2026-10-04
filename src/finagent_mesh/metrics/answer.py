"""Answer quality scorers: normalized EM (official) + token F1 (diagnostic)."""

from __future__ import annotations

import re
import unicodedata


def normalize_answer(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalized_exact_match(prediction: str, label: str) -> float:
    return 1.0 if normalize_answer(prediction) == normalize_answer(label) else 0.0


def token_f1(prediction: str, label: str) -> float:
    pred_toks = normalize_answer(prediction).split()
    label_toks = normalize_answer(label).split()
    if not pred_toks and not label_toks:
        return 1.0
    if not pred_toks or not label_toks:
        return 0.0
    common: dict[str, int] = {}
    for t in label_toks:
        common[t] = common.get(t, 0) + 1
    overlap = 0
    for t in pred_toks:
        if common.get(t, 0) > 0:
            overlap += 1
            common[t] -= 1
    if overlap == 0:
        return 0.0
    precision = overlap / len(pred_toks)
    recall = overlap / len(label_toks)
    return 2 * precision * recall / (precision + recall)
