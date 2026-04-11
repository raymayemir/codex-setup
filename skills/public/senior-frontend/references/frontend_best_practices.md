# Frontend Best Practices

Use this checklist for production-quality frontend delivery across features, refactors, and reviews.

## Architecture And Boundaries

- Keep domain logic outside UI components.
- Keep shared UI primitives in a stable design-system layer.
- Favor composition over inheritance and giant utility modules.
- Define feature boundaries by route or business capability.

## Reliability And Correctness

- Enforce TypeScript strictness for new modules.
- Validate external API responses at boundaries.
- Keep nullability explicit in props and server data contracts.
- Fail fast on impossible states.

## Performance And UX

- Prioritize `async-*`, `bundle-*`, and `server-*` rules first.
- Optimize for perceived speed: stream early, hydrate less, defer non-critical JS.
- Avoid rerender micro-tuning until data flow is clean.
- Use skeletons and transitions for non-blocking feedback.

## Accessibility

- Keep semantic HTML as default.
- Ensure keyboard access for all interactions.
- Keep visible focus states and proper labels.
- Test with screen-reader-friendly landmarks and heading hierarchy.

## Security

- Do not trust client input; validate on server.
- Avoid dangerous HTML injection unless sanitized and audited.
- Keep auth checks in server actions and API routes.
- Avoid exposing secrets in client bundles.

## Testing Strategy

- Unit-test pure logic and state transitions.
- Integration-test critical user flows.
- E2E-test authentication, checkout/payment, and mission-critical paths.
- Keep flaky tests quarantined and tracked.

## CI Quality Gates

- `lint` must pass.
- `typecheck` must pass.
- `test` must pass.
- Production build must pass.
- Critical web-vitals regression must block merge.

## Code Review Checklist

- Is the data flow obvious and minimal?
- Is the server/client boundary intentional?
- Are selected performance rule IDs documented?
- Are accessibility and security constraints covered?
- Are tests proportional to risk?
