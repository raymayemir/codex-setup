# React Patterns

Use these patterns for component architecture and state flow before introducing micro-optimizations.

## Build Server-First Boundaries

- Keep data fetching and data shaping in server components when possible.
- Move interactivity into the thinnest possible client component.
- Pass minimal serialized props across server/client boundaries.
- Cross-reference: `vercel-react-best-practices/rules/server-serialization.md`.

## Prefer Explicit Composition

- Compose small components with clear ownership of data and side effects.
- Avoid deep prop drilling by moving repeated behavior into hooks or context providers scoped to a feature.
- Avoid global state for local UI concerns.

## Keep State Minimal and Derived

- Store source-of-truth state only.
- Derive booleans and computed values during render when possible.
- Avoid effect-driven derived state unless external systems require it.
- Cross-reference:
  - `vercel-react-best-practices/rules/rerender-derived-state.md`
  - `vercel-react-best-practices/rules/rerender-derived-state-no-effect.md`

## Stabilize Dependencies and Callbacks

- Use primitive dependencies in effects.
- Prefer functional `setState` updates for callback stability.
- Hoist non-primitive defaults outside render scope.
- Cross-reference:
  - `vercel-react-best-practices/rules/rerender-dependencies.md`
  - `vercel-react-best-practices/rules/rerender-functional-setstate.md`
  - `vercel-react-best-practices/rules/rerender-memo-with-default-value.md`

## Place Expensive Work Deliberately

- Keep simple expressions inline; avoid `useMemo` for trivial primitives.
- Memoize expensive tree branches by extracting subcomponents.
- Use `startTransition` for non-urgent updates.
- Cross-reference:
  - `vercel-react-best-practices/rules/rerender-simple-expression-in-memo.md`
  - `vercel-react-best-practices/rules/rerender-memo.md`
  - `vercel-react-best-practices/rules/rerender-transitions.md`

## Move Interaction Logic To Events

- Put user-triggered side effects directly in event handlers.
- Keep effects for synchronization with external systems.
- Use refs for transient values that should not trigger rerenders.
- Cross-reference:
  - `vercel-react-best-practices/rules/rerender-move-effect-to-event.md`
  - `vercel-react-best-practices/rules/rerender-use-ref-transient-values.md`
  - `vercel-react-best-practices/rules/advanced-event-handler-refs.md`

## Example Pattern: Render-Derived State

```tsx
function Search({ items }: { items: string[] }) {
  const [query, setQuery] = useState('');
  const normalized = query.trim().toLowerCase();
  const filtered = useMemo(
    () => items.filter((item) => item.toLowerCase().includes(normalized)),
    [items, normalized],
  );

  return (
    <section>
      <input value={query} onChange={(e) => setQuery(e.target.value)} />
      <ul>{filtered.map((item) => <li key={item}>{item}</li>)}</ul>
    </section>
  );
}
```

## React PR Checklist

- Does each component own a single concern?
- Is state minimal and clearly sourced?
- Are effects only used for external synchronization?
- Are heavy branches memoized only when beneficial?
- Are selected Vercel rule IDs listed in the PR notes?
