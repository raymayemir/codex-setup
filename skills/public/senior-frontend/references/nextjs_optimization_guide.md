# Next.js Optimization Guide

Use this guide for App Router performance work and Next.js refactors.

## 1. Remove Fetch Waterfalls First

- Start independent async work early.
- Await late, close to actual usage.
- Use `Promise.all` for independent dependencies.
- Add Suspense boundaries to stream independent sections.
- Cross-reference:
  - `vercel-react-best-practices/rules/async-parallel.md`
  - `vercel-react-best-practices/rules/async-defer-await.md`
  - `vercel-react-best-practices/rules/async-suspense-boundaries.md`

## 2. Reduce JavaScript Sent To The Client

- Replace barrel imports with direct imports for hot paths.
- Lazy-load heavy UI with `next/dynamic`.
- Defer analytics and non-critical third-party code.
- Preload likely-needed modules on hover or focus.
- Cross-reference:
  - `vercel-react-best-practices/rules/bundle-barrel-imports.md`
  - `vercel-react-best-practices/rules/bundle-dynamic-imports.md`
  - `vercel-react-best-practices/rules/bundle-defer-third-party.md`
  - `vercel-react-best-practices/rules/bundle-preload.md`

## 3. Optimize Server Runtime Behavior

- Use request-level deduplication with `React.cache()` when data is reused.
- Add bounded cross-request caches only for truly reusable data.
- Minimize serialized payload passed to client components.
- Authenticate server actions exactly like API routes.
- Cross-reference:
  - `vercel-react-best-practices/rules/server-cache-react.md`
  - `vercel-react-best-practices/rules/server-cache-lru.md`
  - `vercel-react-best-practices/rules/server-serialization.md`
  - `vercel-react-best-practices/rules/server-auth-actions.md`

## 4. Keep Client Fetching Predictable

- Use SWR or equivalent dedup-aware client fetching for shared endpoints.
- Avoid duplicate global event listeners in feature components.
- Keep localStorage schema versioned and compact.
- Cross-reference:
  - `vercel-react-best-practices/rules/client-swr-dedup.md`
  - `vercel-react-best-practices/rules/client-event-listeners.md`
  - `vercel-react-best-practices/rules/client-localstorage-schema.md`

## 5. Validate Hydration And Rendering Stability

- Use explicit conditional rendering (`condition ? <A/> : null`) when behavior is ambiguous.
- Use targeted hydration mismatch suppression only when expected and documented.
- Prefer transition-based UX updates over custom loading toggles.
- Cross-reference:
  - `vercel-react-best-practices/rules/rendering-conditional-render.md`
  - `vercel-react-best-practices/rules/rendering-hydration-suppress-warning.md`
  - `vercel-react-best-practices/rules/rendering-usetransition-loading.md`

## 6. Measure Before And After

Collect evidence for each optimization:

- `next build` output (bundle/chunk deltas)
- Web Vitals deltas (LCP, INP, CLS)
- Server timings for high-traffic routes
- Hydration warnings and runtime error count

Reject changes that increase complexity without measurable benefit.
