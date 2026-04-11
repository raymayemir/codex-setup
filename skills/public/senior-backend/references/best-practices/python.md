# Python Backend Best Practices (Senior)

## 1. Architecture and Modularity

- Separate transport (FastAPI/Flask/Django views), application services, and infrastructure adapters.
- Keep framework-specific code at boundaries; core logic should be framework-agnostic.
- Use explicit dependency wiring (constructors/factories) instead of hidden globals.
- Keep modules cohesive and small; enforce import boundaries in larger codebases.

## 2. API and Data Contracts

- Define strict request/response schemas (Pydantic/dataclasses/DRF serializers).
- Version public APIs and publish deprecation windows.
- Normalize validation errors into a consistent envelope.
- Make write operations idempotent where retries are possible.

## 3. Async, Concurrency, and I/O Discipline

- Do not mix sync blocking I/O inside async endpoints.
- Use bounded task concurrency (`Semaphore`, worker pools) for fan-out patterns.
- Set per-request and downstream timeouts explicitly.
- Propagate cancellation and deadlines to HTTP/DB clients.

## 4. Error Handling and Resilience

- Use domain exceptions for business branches and map them once at API boundary.
- Preserve original exception context (`raise ... from exc`).
- Avoid broad `except Exception` unless re-raising with strict fallback behavior.
- Implement retries only for transient failures, with exponential backoff and jitter.

## 5. Observability

- Emit structured JSON logs with stable fields: `service`, `trace_id`, `request_id`, `tenant_id` when allowed.
- Add metrics for request rate, error rate, latency, queue depth, and retry count.
- Trace all outbound calls (DB, cache, queues, external APIs).
- Add health/readiness checks that validate critical dependencies.

## 6. Data and Transactions

- Use explicit transaction scopes; avoid long-lived transactions.
- Guard against race conditions on shared writes (optimistic locking/version columns).
- Keep migrations reversible when possible and backward-compatible across rolling deploys.
- Add indexes intentionally and validate query plans on hot paths.

## 7. Performance

- Measure first (`py-spy`, profiling middleware, DB query logs).
- Avoid per-request dynamic imports and repeated expensive object construction.
- Cache only with clear invalidation semantics and bounded TTL.
- Stream large responses; avoid loading multi-MB payloads in memory unnecessarily.

## 8. Security

- Treat all external input as untrusted; validate and constrain sizes.
- Enforce authn/authz consistently and centrally.
- Use parameterized SQL and safe ORM patterns; never string-concatenate queries.
- Keep secrets in dedicated secret managers; rotate credentials.
- Add rate limiting and request body limits for abuse resistance.

## 9. Testing and Quality Gates

- Use `pytest` with layered strategy: unit, service, integration, and contract tests.
- Mock only true external boundaries; keep domain tests close to real behavior.
- Add static checks (`ruff`, `mypy`/`pyright`) in CI.
- Run migration tests and rollback checks for schema changes.

## 10. Delivery and Runtime Safety

- Pin dependencies and monitor CVEs.
- Keep worker/process/thread model explicit (Gunicorn/Uvicorn/Celery tuning).
- Use graceful shutdown hooks to drain in-flight requests/jobs.
- Make feature flags and rollback procedures standard for risky releases.

## Senior Review Checklist

- Can this endpoint fail safely and observably under downstream outages?
- Are retries bounded and idempotency guaranteed where needed?
- Are timeout values explicit and justified by SLOs?
- Is schema evolution safe for rolling deploys?
- Can incident responders identify cause quickly from telemetry?
