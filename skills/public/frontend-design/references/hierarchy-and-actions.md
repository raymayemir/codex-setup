# Hierarchy And Actions

Use this reference for any interface with multiple actions, dense information, labels, metrics, or repeated components.

## Hierarchy Is The Main Design Tool

When everything competes for attention, nothing feels designed. Decide what matters most, then make the rest support it.

Rank the content:
- one primary action or message
- a few secondary actions or supporting details
- tertiary actions and passive information

If an element is supposed to lead, it should win in contrast, weight, placement, or surrounding space.

## Emphasize By De-Emphasizing

When the primary item does not stand out, reduce the visual energy of its competitors before making it louder.

Useful levers:
- softer text color for secondary items
- less prominent button treatment for non-primary actions
- reduced icon contrast
- smaller clusters of helper content
- more breathing room around the important thing

## Do Not Use Size Alone

Relying only on font size often creates oversized headlines and tiny secondary text. Use a mix of:
- font weight
- contrast
- spacing
- placement
- container treatment

Large type should be earned by actual importance.

## Labels Are Often Overused

Avoid turning every piece of data into `Label: Value`.

Prefer:
- context that makes the value obvious
- formatting that communicates the type of data
- grouped presentations where labels are visually secondary

Use explicit labels when ambiguity would slow the user down or harm accessibility.

## Semantics And Presentation Are Separate

Use the right semantic markup, but do not let browser defaults dictate visual hierarchy. A semantic page title does not always need oversized `h1` styling in an application UI.

## Action Design

Design actions as a pyramid:
- Primary: obvious, high-contrast, singular when possible
- Secondary: present but quieter
- Tertiary: text buttons, icon buttons, row actions, or menu actions
- Destructive: clear but not accidentally dominant unless the page is explicitly about a destructive choice

If a page seems to have three primary buttons, it probably has zero.

## Quick Checks

- Can a user identify the main action in three seconds?
- Are supporting actions visually quieter than the primary one?
- Does spacing show which labels, fields, and helper text belong together?
- Does the interface still make sense if you mute most accent colors?
