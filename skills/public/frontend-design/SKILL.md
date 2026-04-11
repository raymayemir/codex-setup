---
name: frontend-design
description: Design and implement production-grade web interfaces using a feature-first, hierarchy-first workflow. Use when building or refactoring pages, dashboards, forms, landing pages, components, or any frontend UI that needs stronger layout, spacing, typography, color, and finishing quality.
license: Complete terms in LICENSE.txt
---

# Frontend Design

Design and implement production-grade interfaces with a strong visual point of view and strong structural discipline.

This skill is for visual design work that must end in real frontend code. Use it for calm product UIs, polished dashboards, landing pages, dense internal tools, and expressive marketing surfaces. Do not default to maximalism; choose the level of personality that fits the product and audience.

## Execute This Workflow

1. Classify the surface and constraints.
- Identify the interface type: form, settings page, dashboard, landing page, empty state, data table, workflow tool, marketing section, or full application shell.
- Identify the real constraints before styling: audience, accessibility, responsiveness, existing design system, implementation stack, and whether the task is a new surface or a refactor.
- If the request is mostly about frontend architecture or performance rather than visual design, pair with `senior-frontend` instead of stretching this skill past its purpose.

2. Start from the feature, not the shell.
- Design the core user task and primary action flow first.
- Do not begin with navbar, sidebar, page chrome, or decorative layout scaffolding unless the task is explicitly about those surfaces.
- For new work, read `/references/starting-from-scratch.md`.

3. Choose personality and density on purpose.
- Decide how the interface should feel: sober product UI, polished product UI with character, or expressive marketing/editorial UI.
- Make explicit choices for type direction, corner treatment, copy tone, visual density, and interaction energy.
- Personality is required, but "unexpected" is not the goal by itself. Fit and clarity come first.

4. Define systems before decoration.
- Reuse an existing design system when one already exists. If none exists, define a constrained set of values for spacing, type scale, weights, color shades, radius, and elevation before refining visuals.
- Avoid arbitrary one-off values unless there is a compelling visual reason.
- Read the references that match the task:
  - `/references/layout-and-spacing.md`
  - `/references/text-and-typography.md`
  - `/references/color-systems.md`

5. Build hierarchy before polish.
- Identify one primary action, a small number of secondary actions, and any tertiary actions.
- Use contrast, weight, spacing, grouping, and placement before reaching for larger type, extra borders, or louder color.
- For dashboards, forms, settings, and data-heavy tools, always read `/references/hierarchy-and-actions.md`.

6. Add depth, imagery, and finishing touches only after the structure works.
- Use shadows, overlap, accents, decorative backgrounds, and motion only when they strengthen emphasis, depth, or atmosphere.
- Empty states, loading states, and sparse datasets deserve as much care as the "happy path".
- Read `/references/depth-images-and-finishing.md` before adding polish.

7. Check anti-patterns before delivery.
- Read `/references/anti-patterns.md`.
- Validate that the UI still reads clearly on both desktop and mobile, keeps strong action hierarchy, and does not rely on decoration to hide weak structure.

## Reference Routing

- Use `/references/starting-from-scratch.md` for new surfaces, redesigns, or when the request is vague and the structure needs to be discovered.
- Use `/references/hierarchy-and-actions.md` for forms, settings pages, dashboards, tables, CRUD tools, and any interface with competing actions or lots of information.
- Use `/references/layout-and-spacing.md` when the layout feels messy, crowded, over-stretched, or inconsistently grouped.
- Use `/references/text-and-typography.md` when readability, copy presentation, labels, headings, metrics, or table text need work.
- Use `/references/color-systems.md` when defining or cleaning up palettes, neutral ramps, accents, status colors, or contrast handling.
- Use `/references/depth-images-and-finishing.md` for shadows, overlap, image handling, empty states, accent borders, background treatment, and the last 10 percent of polish.
- Always end with `/references/anti-patterns.md`.

## Mandatory Quality Bar

- The main user task must be obvious within a few seconds.
- The primary action must be visually dominant without making every other action loud.
- Spacing must show grouping clearly; adjacent groups should not feel ambiguous.
- Typography must be readable and intentional, not an accumulation of random sizes.
- Color must come from a system of neutrals, core accents, and state colors instead of ad hoc picks.
- Depth, borders, motion, and decoration must add meaning, not noise.
- Empty, loading, error, and user-generated-content states must be handled intentionally.
- The design must hold together on both desktop and mobile.

## Default Visual Philosophy

- Calm, clear product UI is as valid as expressive UI.
- Neutral fonts are acceptable when they serve readability and product fit.
- Distinctiveness comes from composition, hierarchy, restraint, and consistency as much as from novelty.
- "Beautiful" is not enough; the interface should communicate what matters, what belongs together, and what to do next.
