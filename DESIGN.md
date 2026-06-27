---
name: Sudoku
description: A precise, full-stack Sudoku tool that generates, solves, and validates puzzles.
colors:
  accent: "#1565c0"
  accent-deep: "#0d47a1"
  page: "#f0f0f0"
  surface: "#ffffff"
  surface-given: "#e2e2e2"
  ink: "#111111"
  ink-body: "#222222"
  border-cell: "#bbbbbb"
  border-ui: "#333333"
  state-same: "#dbeeff"
  state-selected: "#90caf9"
  state-error-bg: "#f8d7da"
  state-error-ink: "#c62828"
  state-error-selected: "#f1a7ad"
  feedback-warn-bg: "#fff3cd"
  feedback-warn-border: "#ffc107"
  feedback-warn-ink: "#7a5700"
  feedback-success-bg: "#d4edda"
  feedback-success-ink: "#155724"
  feedback-success-border: "#c3e6cb"
  feedback-error-ink: "#721c24"
  feedback-error-border: "#f5c6cb"
typography:
  display:
    fontFamily: "Georgia, serif"
    fontSize: "2.5rem"
    fontWeight: 400
    letterSpacing: "0.15em"
    lineHeight: 1.1
  body:
    fontFamily: "Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1
rounded:
  sm: "4px"
  none: "0px"
spacing:
  xs: "0.4rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.25rem"
  xl: "2rem"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1.25rem"
  button-primary-hover:
    backgroundColor: "{colors.accent-deep}"
    textColor: "#ffffff"
  button-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1.25rem"
  button-default-hover:
    backgroundColor: "{colors.border-ui}"
    textColor: "#ffffff"
  cell-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
  cell-given:
    backgroundColor: "{colors.surface-given}"
    textColor: "{colors.ink}"
  cell-user-filled:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
  cell-selected:
    backgroundColor: "{colors.state-selected}"
    textColor: "{colors.ink}"
  cell-error:
    backgroundColor: "{colors.state-error-bg}"
    textColor: "{colors.state-error-ink}"
  num-btn:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  message-warn:
    backgroundColor: "{colors.feedback-warn-bg}"
    textColor: "{colors.feedback-warn-ink}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1.25rem"
  message-success:
    backgroundColor: "{colors.feedback-success-bg}"
    textColor: "{colors.feedback-success-ink}"
    rounded: "{rounded.sm}"
    padding: "0.5rem 1.25rem"
---

# Design System: Sudoku

## 1. Overview

**Creative North Star: "The Ruled Grid"**

The Ruled Grid is a design vocabulary derived from the logic of the puzzle itself. The 9×9 board is not dressed up — it *is* the interface. Every design decision defers to a single question: does this serve the act of solving? The aesthetic is that of technical drawing — precise ink on a neutral field, not warm, not decorative, not themed. Quality is earned through specificity: which shade of blue marks the user's hand; which shade of gray signals a clue that cannot be changed; the exact weight ratio between the interior cell line and the box boundary that partitions nine regions.

This system rejects the overcrowded game-UI aesthetic — badges, streaks, score counters, pop-up overlays, dark-pattern mechanics — as categorically wrong for what this product is. It equally rejects the generic SaaS template: rounded card grids, gradient buttons, and the reflexive institutional blue that signals "used a UI kit." The grid already has strong enough visual logic that the interface needs only to clarify it, not decorate it.

As a portfolio project, the design proves technical judgment through restraint. The signal is in the states — selected, given, error, success — each distinct and deliberate, each communicating without ornamentation.

**Key Characteristics:**
- Single-page tool with zero navigation chrome; the board is the whole screen
- Cell states (given, user-filled, selected, same-number, error) are the primary visual vocabulary
- One accent color, used only where the user acts or initiates action
- Completely flat; depth conveyed by tonal contrast and border weight alone
- One font family carries every typographic role: heading, controls, messages, grid digits

## 2. Colors: Tonal Clarity

The palette is structured around three tiers: the neutral field that recedes, the precision accent that marks the user's hand, and the semantic state colors that communicate puzzle logic without decoration.

### Primary
- **Steel Authority** (#1565c0): The only chromatic accent in the system. Used exclusively for: user-filled digit color and primary action button background/border. Never decorative. This blue is where the user's hand is — editable space and initiated action, nothing else.
- **Deep Authority** (#0d47a1): The hover descent of Steel Authority. Appears only as the button-primary hover state. One step darker, same hue.

### Neutral
- **Field Gray** (#f0f0f0): The page background — achromatic, cool, and receding. Exists so the white board and cells read as foreground without requiring contrast from color.
- **Surface White** (#ffffff): Cells at rest, buttons at rest. The active surface of the system. Where work happens.
- **Clue Gray** (#e2e2e2): The cells that arrived with the puzzle. Visually subordinate to white — the tonal step that marks immutability. Not interactive.
- **Grid Ink** (#111111): The highest-contrast value. Used only for the board's outer border, the 3×3 box boundaries, and the page heading. These are structural lines; their weight is the point.
- **Body Ink** (#222222): Body text — one step lighter than Grid Ink, enough to preserve contrast while easing the harshness of pure black on gray.
- **Cell Line** (#bbbbbb): The 1px borders between individual cells. Visible enough to give the grid structure; recessive enough not to compete with the 3px box boundaries.
- **UI Line** (#333333): Button borders and hover fill. Weighty but not Grid Ink — the control vocabulary sits one step below the board in visual hierarchy.

### State Colors
- **Sibling Tint** (#dbeeff): The soft blue applied to cells sharing a number with the selection. Indicates mathematical relationship, not user action. Low saturation by design — it whispers, not shouts.
- **Selection Blue** (#90caf9): The active selected cell. Saturated enough to be instantly located; still light enough to remain legible with dark text.
- **Error Field** (#f8d7da): A contradiction detected — a duplicate in a row, column, or box. Never used without the accompanying text color change (#c62828), because color is not the sole error indicator.
- **Error Ink** (#c62828): Error digit color inside cells. The text change enforces the error signal structurally — removing the color does not hide the error, it only loses the channel.
- **Error Selection** (#f1a7ad): The mid-blend that appears when an error cell is also selected — neither pure error nor pure selection, but an unmistakable compound state.

### Feedback Colors (Messages)
- **Warn:** Background #fff3cd, border #ffc107, text #7a5700 — used for informational messages (hints, loading states, ambiguous results).
- **Success:** Background #d4edda, border #c3e6cb, text #155724 — used for puzzle-solved confirmation.
- **Error (message):** Background #f8d7da (shared with cell error state), border #f5c6cb, text #721c24 — used for unsolvable-state and backend-failure messages.

### Named Rules

**The One Accent Rule.** #1565c0 appears in exactly two roles: user-filled digit color, and primary button background. It marks where the user is and what the user can do. Apply it to a decorative element and the semantic contract breaks.

**The Two-Signal Error Rule.** Error states always change both background color AND text/border color. Color alone is not a sufficient indicator (WCAG 1.4.1). The cell error state (#f8d7da bg + #c62828 text) and the error message (#f8d7da bg + #721c24 text) both enforce this.

## 3. Typography: The One-Voice System

**Display / Body / Label Font:** Georgia, serif (no secondary family)

**Character:** Georgia's proportional serifs carry authority without the generic-tool feel of system sans. For a number puzzle, the numerals are the content; the typography around them is a frame. A single, consistent serif keeps that frame unified and legible without asking the user to register two typographic personalities.

### Hierarchy

- **Display** (400 weight, 2.5rem, letter-spacing 0.15em, line-height 1.1): The page heading "Sudoku" only. Wide-tracking creates presence without size inflation. Mobile drops to 1.6rem.
- **Body** (400 weight, 1rem, line-height 1.5): Buttons, controls, difficulty selector, message text. The workhorse size.
- **Label** (400 weight, 1rem, line-height 1): Number pad labels, button loading states. Same size as body; context distinguishes role.
- **Cell digit** (400/700 weight, ~25px at max cell size via `calc(var(--cell) * 0.48)`): The grid's numbers. User-filled at 400 weight in Steel Authority (#1565c0); given clues at 700 weight in Grid Ink (#111111). The weight contrast reinforces the color distinction — two orthogonal signals for the same semantic difference.
- **Success message** (700 weight, 1.2rem): The only enlarged feedback text. Emphasis on the completion moment.

### Named Rules

**The One Family Rule.** No secondary font is introduced. Georgia carries the heading, the controls, the messages, and (through inheritance) the grid digits. Any temptation to switch to a sans-serif for "efficiency" should be resisted — the serif is the brand signal.

**The Weight Contrast Rule.** Given clues (700) and user-filled digits (400) differ in weight *and* color. Never communicate immutability through color alone.

## 4. Elevation

This system is completely flat. No shadows exist anywhere. Depth is conveyed through three mechanisms only: tonal contrast between page gray (#f0f0f0) and surface white (#ffffff); border weight contrast between the 1px cell line (#bbbbbb) and the 3px box boundary (#111111); and background state changes that shift cell colors without lift.

**The Flat-By-Default Rule.** Surfaces never lift. `box-shadow` is prohibited at any scale. The grid's depth comes from the structural weight of its ink, not from simulated light sources. If you feel the urge to add a shadow, add tonal contrast or border weight instead.

## 5. Components

### The Sudoku Board

The board is the primary component — a 9×9 CSS Grid driven by a single custom property `--cell` (clamped between 36px and 52px based on viewport width). This single variable controls board width, cell dimensions, digit size, and number pad button sizing. It is the design system's one layout token.

- **Outer border:** 3px solid #111111 — the container of the game
- **Box boundaries:** 3px solid #111111 on `.box-border-right` (columns 3, 6) and `.box-border-bottom` (rows 3, 6) — the regional divisions
- **Cell borders:** 1px solid #bbbbbb — the individual cell grid
- **No border radius** — the board's sharp corners are intentional

### Cells

The cell state vocabulary is the most expressive part of the system. All states use `transition: background-color 0.08s`.

- **Default:** White (#ffffff) background, 1px #bbbbbb border. Cursor: pointer.
- **Given (clue):** #e2e2e2 background, 700 weight, #111111 color. Cursor: default. Not interactive.
- **User-filled:** White background, #1565c0 digit color, 400 weight. The accent marks the user's work.
- **Selected:** #90caf9 background (via `!important` — overrides sibling and default). The active cell.
- **Same-number:** #dbeeff background — cells containing the same digit as the selected cell. Secondary signal; lower priority than selection.
- **Error:** #f8d7da background, #c62828 text, 700 weight (via `!important`). Conflict detected.
- **Error + Selected:** #f1a7ad background — the compound state when the selected cell is in error.

### Buttons

All buttons share a common shape vocabulary: 4px border radius, 2px border, 1rem Georgia font, `0.5rem 1.25rem` padding. `transition: background-color 0.12s, color 0.12s`.

- **Primary (`.btn-primary`):** #1565c0 fill and border, white text. Hover: #0d47a1. Used for "New Game" and "Check Puzzle" — the initiating actions.
- **Default (`.btn`):** White fill, #333333 border, #111111 text. Hover: #333333 fill, white text. Used for all secondary actions: Hint, Solve, Create Puzzle, Back to Play, Clear Grid.
- **Disabled:** 0.38 opacity, `cursor: not-allowed`. Applied on both variants.
- **Loading state:** A 14×14 CSS spinner (2px border, `spin` animation at 0.6s linear) alongside a text label, using `display: inline-flex; gap: 0.4rem`.

The difficulty `<select>` uses the same visual vocabulary as buttons (2px solid #333333 border, 4px radius, white background, 1rem Georgia) so it reads as part of the same control tier.

### Number Pad

A 5-column grid of buttons (1–9 plus a "Clear" button). Each button is styled identically to the default `.btn` except height is derived from `calc(var(--cell) * 0.85)` — it scales with the board. The "Clear" label uses a smaller font size (0.85rem) and wider letter spacing (0.04em) to distinguish it from digit buttons without changing shape.

### Messages

A single `.message` class with three modifier variants. All use 4px radius, `0.5rem 1.25rem` padding, 1px border, 1rem Georgia.

- **Warning (default):** #fff3cd / #ffc107 / #7a5700 — informational states, hint feedback
- **Success (`.message.success`):** #d4edda / #c3e6cb / #155724, 1.2rem, 700 weight — puzzle completion
- **Error (`.message.error`):** #f8d7da / #f5c6cb / #721c24 — failure states, backend errors

## 6. Do's and Don'ts

### Do:
- **Do** reserve #1565c0 (Steel Authority) for user-filled digit color and primary action buttons only. Its rarity is the semantic contract.
- **Do** use 3px solid #111111 for board and box boundaries, and 1px #bbbbbb for cell boundaries. This two-weight contrast is the grid's visual structure.
- **Do** derive any grid-adjacent sizing from the `--cell` custom property so the entire board scales from a single token.
- **Do** mark errors with both background color AND text color change (WCAG 1.4.1 — color is not the sole indicator).
- **Do** maintain the weight distinction between given cells (700 weight) and user-filled cells (400 weight). Two independent channels for the same semantic difference.
- **Do** keep focus indicators visible: 2px solid accent (primary) or 2px solid #333333 (default) at 2px offset.
- **Do** use the existing semantic classes when adding new cell-adjacent states — don't introduce new background colors outside the state vocabulary.

### Don't:
- **Don't** add `box-shadow` to any surface. The system is flat. Shadows are prohibited at all scales.
- **Don't** add a second typeface. Georgia is the only family. Mixing sans-serif controls into a serif frame breaks the One-Voice system.
- **Don't** use border-left or border-right greater than 1px as a colored accent on messages, alerts, or any container. Use full borders, background tints, or no border at all.
- **Don't** apply the accent color (#1565c0) to inactive states, decorative elements, icons, or section accents. Outside its two defined roles, it becomes noise.
- **Don't** round the board's corners. The `border-radius: 0` on `.board` is deliberate — the grid has sharp geometry.
- **Don't** introduce the mobile-game aesthetic: no badges, streak counters, achievement unlocks, pop-up modals, or reward animations. The puzzle is the product.
- **Don't** use gradient text (`background-clip: text`), glassmorphism, or decorative blur effects. These are categorically wrong for this register.
- **Don't** use generic template components: identical card grids, gradient buttons, or side-stripe bordered callouts.
- **Don't** soften the state vocabulary. Each cell state exists because it communicates something specific about the puzzle. Merging or omitting states to "simplify" the visual removes real information.
