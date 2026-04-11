# Golang Backend Best Practices (Senior)

## 1. Architecture and Boundaries

- Define clear package boundaries: `internal/` for private code, small `pkg/` only when reuse is proven.
- Keep handlers thin; move business logic into services/use-cases.
- Isolate external systems behind interfaces only where test seams are needed.
- Make dependency direction explicit: transport -> service -> repository, never reverse.

## 2. API and Contract Design

- Version public APIs intentionally (`/v1`, schema evolution plan).
- Return stable error envelopes and map internal errors to explicit client-safe codes.
- Validate input at the transport boundary and normalize before business logic.
- Support idempotency for unsafe operations (idempotency key or natural key checks).

## 3. Concurrency, Context, and Cancellation

- Pass `context.Context` as first argument in request-scoped calls.
- Never store `Context` in structs.
- Respect cancellation in DB, HTTP, and goroutines.
- Avoid unbounded goroutine creation; use worker pools and bounded queues.
- Protect shared state with clear ownership; prefer channels for coordination, mutexes for critical sections.

## 4. Error Handling

- Return errors, do not panic in normal control flow.
- Wrap with `%w` and preserve root cause.
- Use sentinel or typed errors only for actionable branches.
- Log errors once at boundary layers to avoid duplicate noisy logs.

## 5. Observability

- Emit structured logs (JSON) with stable keys: `service`, `trace_id`, `span_id`, `request_id`, `user_id` when allowed.
- Record RED metrics for HTTP/gRPC: rate, errors, duration.
- Instrument traces for all I/O boundaries (DB, cache, queue, third-party).
- Add domain-specific counters/histograms for key business flows.

## 6. Database and Consistency

- Use explicit transaction boundaries and keep transactions short.
- Prefer optimistic concurrency where contention is moderate.
- Make migrations backward-compatible first, then cleanup in later deploy.
- Use timeouts and context on every query.
- Prevent N+1 queries and full-table scans on hot paths.

## 7. Performance and Resource Safety

- Profile before optimizing (`pprof`, traces, benchmark tests).
- Minimize allocations in hot code; reuse buffers when measurable.
- Set explicit HTTP server/client timeouts.
- Cap payload sizes and stream large responses where possible.

## 8. Security

- Enforce authn/authz in middleware and re-check critical permissions in service layer.
- Validate and sanitize all untrusted input.
- Avoid leaking internals in client-facing errors.
- Store secrets in managed secret stores, never in code or logs.
- Add rate limiting and abuse protection for expensive endpoints.

## 9. Testing Strategy

- Keep most tests at service layer with deterministic fakes.
- Add contract tests for transport layer and serialization.
- Use integration tests for DB migrations and transactional correctness.
- Use race detector and run it in CI for relevant packages.

## 10. Delivery and Operations

- Keep builds reproducible and pinned.
- Add readiness/liveness checks based on real dependencies.
- Ship with safe defaults: conservative timeouts, retries with jitter, bounded concurrency.
- Define rollback and feature-flag strategy for risky changes.

## Senior Review Checklist

- Are failure modes explicit and observable?
- Are retries bounded, idempotent, and jittered?
- Is data consistency strategy documented per write path?
- Are latency budgets and timeout values justified?
- Can on-call diagnose incidents from logs/metrics/traces without code archaeology?
