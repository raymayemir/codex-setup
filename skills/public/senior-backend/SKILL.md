---
name: senior-backend
description: Senior backend engineering guidance for architecture, implementation, refactoring, and review of production services. Use when tasks involve backend APIs, distributed systems, reliability hardening, performance tuning, security controls, data consistency, or incident-prone code paths in Golang or Python.
---

# Senior Backend

Plan and implement backend work with senior-level production constraints first: correctness, safety, operability, and long-term maintainability.

## Execute This Workflow

1. Classify the task before coding.
- Detect request type: feature implementation, refactor, debugging, review, performance, security, or reliability hardening.
- Detect runtime and boundaries: service role, data stores, external dependencies, latency budget, and failure domains.
- Read current code paths and dependency usage before touching files.

2. Select the language guide and load only needed references.
- For Go services, load `/references/best-practices/golang.md`.
- For Python services, load `/references/best-practices/python.md`.
- If the task spans both, apply shared principles first and language specifics second.

3. Design for operations, then code.
- Define contracts and error semantics before implementation.
- Make idempotency, observability, and rollback strategy explicit.
- Prefer small composable modules and deterministic behavior over framework magic.

4. Use the helper script to quickly load or export standards.
- Run `python scripts/backend_best_practices.py list`.
- Run `python scripts/backend_best_practices.py show --language golang`.
- Run `python scripts/backend_best_practices.py export --language python --output docs/python-backend-standards.md`.

5. Validate and ship.
- Run language-specific tests, linters, and type checks.
- Verify structured logs, metrics, and traces exist for critical paths.
- Confirm migrations, timeouts, retries, and authz rules are explicit and tested.

## Output Requirements

- Explain key tradeoffs (simplicity, latency, safety, cost).
- Surface failure modes and mitigation strategy.
- Prefer minimal diff with clear behavior changes.
- Reject unsafe defaults: missing timeouts, unbounded retries, weak validation, silent errors.

## Mandatory Engineering Discipline

- Do not change code until full context is understood: call flow, existing abstractions, and dependency behavior.
- Inspect dependencies and current wrappers before implementation; do not re-implement behavior already provided by libraries.
- Reuse existing functions, services, utilities, and helpers whenever possible; add new abstractions only for real gaps.
- Leave no code trash: remove temporary debug code, unused imports, dead helpers, commented-out blocks, and stale TODOs.
- Optimize for both clarity and efficiency: prefer predictable, measurable improvements over speculative rewrites.

## Reference Map

- `/references/best-practices/golang.md`
- `/references/best-practices/python.md`
