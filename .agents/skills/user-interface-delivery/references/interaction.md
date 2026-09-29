# Interaction Reference

## Direct workflows and forms

- Ask only for required information; use visible, changeable defaults where reliable.
- Validate near the relevant field, preserve valid input, and move focus to useful error context.
- Support paste, autofill, password managers, keyboard submission, and native input behavior where applicable.
- Acknowledge actions promptly, show meaningful progress, prevent accidental duplicates, and preserve safe retry.
- Keep results in the working context unless a separate view materially helps.
- Preserve lengthy or valuable drafts. Explain unavailable actions instead of showing unexplained disabled controls.
- Avoid surprise navigation, hidden requirements, manipulative choices, and unnecessary confirmations.

## Multi-step exception

When multiple steps are justified, show progress, preserve state, allow safe back navigation, and provide a useful final review. Keep advanced or rare options behind progressive disclosure.

## Mobile and extensions

- Request permissions at the point of use and keep unrelated features usable after optional denial.
- Preserve valuable state across suspension, termination, closure, and updates.
- Make offline, reconnecting, synchronized, and stale states clear. Replay offline work only when safe.
- Do not silently overwrite synchronization conflicts.
- Use a larger context for extension workflows that do not fit safely in a small popup.
- Respect battery, bandwidth, storage, and background-execution limits.

## Regional behavior

Use Unicode and unambiguous dates, time zones, numbers, and currencies. Add full localization only when the audience or credible roadmap requires it. Human-review critical legal, safety, financial, and security translations.
