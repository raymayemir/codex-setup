# Color Systems

Use this reference when choosing palettes, building status colors, or cleaning up interfaces that feel chromatically inconsistent.

## Think In Systems, Not One-Off Picks

- Color should come from ramps and roles, not from repeatedly opening a picker.
- HSL-style thinking is useful because hue, saturation, and lightness map better to how designers reason about color.
- Define a small set of named roles before styling: canvas, surface, text, muted text, primary action, accent, success, warning, danger.

## You Need More Than Five Colors

A usable interface usually needs:
- a neutral ramp for backgrounds, borders, and text
- a primary ramp for brand or action emphasis
- optional accent ramps
- state colors for success, warning, and danger

If everything important uses the same single brand color, the interface will run out of hierarchy quickly.

## Define Shades Up Front

Pick stable shades for each ramp instead of generating them ad hoc. A `50-900` style scale is often practical if the product already uses tokenized themes.

The exact naming is less important than consistency.

## Neutrals Can Be Warm Or Cool

True gray is not required. Slightly warm or cool neutrals can add atmosphere while still behaving like neutrals.

## Lightness And Saturation Move Together

Very light or very dark colors often need saturation adjustment to avoid looking washed out or muddy. Do not assume a simple lighten or darken function will produce good UI shades.

## Accessibility Does Not Require Boring Color

- Preserve contrast first.
- If a colored text treatment fails contrast, try darker text on a tinted surface, a deeper hue, or a different shade pairing.
- Validate contrast for body text and small UI text, not just hero headings.

## Never Rely On Color Alone

State changes should also use:
- icons
- labels
- arrows
- badges
- text changes

This matters for color blindness and for quick scanning under poor conditions.

## Quick Checks

- Is there a clear neutral system, not just random grays?
- Are action and status colors distinct in role, not just in hue?
- Do colored surfaces still support readable text?
- Would a color-blind user still understand success, warning, and error states?
