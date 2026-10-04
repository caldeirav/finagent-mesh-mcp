# System-1 Engine Adapter Contract

Harness-facing API remains [001 systemone-openapi.yaml](../../001-finagentbench-harness/contracts/systemone-openapi.yaml): `GET /healthz`, `POST /v1/systemone`.

Adapters live under `src/finagent_mesh/clients/engines/` and translate native engine APIs into that shape (or wrap a sidecar that already speaks it).

## Shared requirements

| Requirement | Rule |
|-------------|------|
| Health | `GET {base_url}/healthz` → `200` + `{ "status": "ok", "engine": "<config_id>" }` |
| Decide | `POST {base_url}/v1/systemone` with `primitive` ∈ supported set |
| Identity | Response MUST include `engine` (= `config_id`) and `model_revision` |
| Fail closed | Unhealthy / timeout → HTTP 503 or client exception; harness MUST NOT mock-substitute |
| Latency | Adapter or sidecar SHOULD record decision `latency_ms` in traces/metadata |

## Per-family adapter notes

### AnyJev (`anyjev.py`) — `anyjev-l0`, `anyjev-l1`

- Primitive: `choice`
- L0: adaptive cyclic shifts; L1: temperature scaling using `calibration_ref` (200 IDs)
- Startup of L1 fails if calibration missing or wrong cardinality

### CLM-8B (`clm8b.py`) — `clm-8b`

- Primitives: `score`, `action_cache`
- Uses pre-computed action embeddings + Action Cache similarity over candidate space
- Typical Stage-2 partner on `:8001`

### vLLM-sr Decision-2.0 (`vllm_sr.py`) — `decision20-kai`, `decision20-lux`

- Primitive: `choice`
- Kai vs Lux selected via weights/env; reported as distinct `config_id` / `model_revision`

### Laya (`laya.py`) — `laya-modernbert`

- Primitive: `choice`
- Local Transformers path; may be edge CPU/GPU; always record latency

### AR baseline (`ar_baseline.py`) — `ar-qwen3-8b-instruct`

- Primitive: `json_choice` (request) → mapped to OpenAPI `choice` ranking in response when parse succeeds
- Prompt for structured JSON e.g. `{"ordered_ids":[...],"scores":[...]}`
- On parse failure: set `parse_failure=1`, fail structured Stage-1 ranking for that example; still record generation latency (and optional logprobs)

## Binding

Pipeline/matrix sets two clients:

```text
stage1_client = adapter_for(stage1_config_id)
stage2_client = adapter_for(stage2_config_id)
```

Matrix row binding rules: [data-model.md](../data-model.md).
