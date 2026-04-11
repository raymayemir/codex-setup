# Vercel React Best Practices Index

Use this index to apply the imported `react-best-practices` material with minimal context load.

## Source

- Upstream repository: `vercel-labs/agent-skills`
- Imported skill: `skills/react-best-practices`
- Local snapshot files:
  - `full-guide.md` (compiled full document)
  - `upstream-skill.md` (upstream SKILL.md snapshot)
  - `rules/*.md` (rule-by-rule files)

## Apply Rules With Minimal Context

1. Open only this file first.
2. Pick the category from symptoms or task type.
3. Load only the exact rule files needed from `rules/`.
4. Apply highest-priority fixes first.
5. Validate with build, tests, and runtime checks.

## Category Selection

- Waterfalls, slow TTFB, sequential fetches:
  - `async-*`
- Large bundles, slow hydration, heavy JS payload:
  - `bundle-*`
- Server action/API throughput, cache inefficiency, large RSC payloads:
  - `server-*`
- Duplicate client fetches/listeners, noisy localStorage patterns:
  - `client-*`
- Frequent rerenders, unstable effects/dependencies:
  - `rerender-*`
- Paint/hydration bottlenecks and visual instability:
  - `rendering-*`
- Tight loops and hot-path JS inefficiencies:
  - `js-*`
- Specialized lifecycle or event-handler patterns:
  - `advanced-*`

## High-Impact Rule Starter Set

Start with these before broader cleanup:

- `rules/async-parallel.md`
- `rules/async-defer-await.md`
- `rules/async-suspense-boundaries.md`
- `rules/bundle-barrel-imports.md`
- `rules/bundle-dynamic-imports.md`
- `rules/bundle-defer-third-party.md`
- `rules/server-cache-react.md`
- `rules/server-parallel-fetching.md`
- `rules/server-serialization.md`
- `rules/rerender-dependencies.md`
- `rules/rerender-derived-state-no-effect.md`
- `rules/rendering-content-visibility.md`

## PR Integration Pattern

When preparing a change:

1. Document selected rule IDs in the PR description.
2. Attach before/after evidence (bundle size, web-vitals, or trace).
3. Keep unrelated style refactors out of the patch.
4. Skip low-priority micro-optimizations unless measurable.

## License Note

The imported upstream material is distributed under MIT in the source repository. Keep attribution when reusing these rule files elsewhere.
