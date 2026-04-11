# Layout And Spacing

Use this reference when the UI feels crowded, vague, too wide, too fluid, or inconsistently grouped.

## Start Too Spacious, Then Tighten

- It is easier to remove space than to discover it late.
- Begin with generous whitespace so relationships are obvious.
- Tighten only where density improves scanning or task speed.
- Dense UIs are valid, but density should be intentional and localized.

## Define A Spacing And Sizing System

If the product does not already have tokens, define a short scale and reuse it everywhere.

Example scale:
- `4, 8, 12, 16, 24, 32, 48, 64, 96`

Use visibly distinct steps. Do not tweak values pixel by pixel while designing.

## Grouping Through Space

Use spacing to show belonging:
- element-to-element spacing inside a control group should be smallest
- spacing between related groups should be larger
- spacing between major sections should be largest

If two relationships use the same spacing, users will read them as equally related.

## Do Not Fill The Whole Screen By Default

- A wider canvas is not automatically a better canvas.
- Forms, settings surfaces, cards, and reading-heavy content often become clearer when constrained to a narrower max width.
- Only use full width when the content truly benefits from it: large data grids, media, maps, or multi-panel workflows.

## Grids Are Useful, Not Sacred

- Use grids to organize, not to outsource all judgment.
- Not every element needs to be fluid.
- Give important components stable widths when it improves readability or scanning.

## Relative Scaling Is Not A Universal Rule

Relationships that work on desktop often need manual adjustment on smaller screens. Do not assume every dimension should shrink by the same percentage.

Prefer breakpoint-specific decisions for:
- headline sizes
- form widths
- panel density
- card layouts
- data table behavior

## Use Fewer Borders

Before adding a border, ask whether spacing, background contrast, or layout separation would communicate the structure more cleanly.

## Quick Checks

- Is the main content area narrower than the screen when it should be?
- Are section, group, and element gaps clearly different?
- Are related controls visually grouped without needing extra borders?
- Does the layout still feel intentional on a small screen?
