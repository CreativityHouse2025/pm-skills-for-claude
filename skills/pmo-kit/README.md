# PMO Kit

Shared rules and one view across many projects.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Captures how your organisation runs projects in one standards sheet
- Produces your own template set with your rules built in
- Checks a project document against your house rules
- Builds a portfolio status report with decisions needed first
- Sets up project intake, prioritisation scoring and stage gates
- Writes a "how we run projects here" handbook

## Who it is for

Operations leads, PMO staff, department heads, owners of companies running several projects.

## Try it

- "We have 8 to 10 client projects and every manager works differently. Help us get consistent."
- "Build one report for leadership from these four project updates, using our colour rules."
- "Rank our five project requests by priority."

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Proposed rules are labelled as suggested until your organisation agrees them
- Status colours are recalculated from the numbers; missing data is shown as missing
- A prioritisation score informs the decision; it does not make it

## Install

**Claude apps:** zip this folder so that `pmo-kit` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `assets/`
  - `standards-sheet.md`
- `evals/`
  - `portfolio-report-rule-based-colours/`
  - `prioritise-without-ratings/`
  - `standards-for-small-agency/`
- `references/`
  - `agile.md`
  - `arabic-terms.md`
  - `catalog.md`
  - `outputs.md`
  - `review-checklists.md`
- `README.md`, `LICENSE`: this page and the licence

`evals/` holds 3 test cases. Each has a prompt, the expected outcome and the checks a good answer must pass.

## Status

Version 0.1.0, pre-release. See the [changelog](../../CHANGELOG.md). Problems and suggestions are welcome through the repository's issues.

## Licence

MIT. See [LICENSE](LICENSE).

---

<div dir="rtl">

## بالعربية

لمن يدير عدة مشاريع: يكتب قواعد المؤسسة مرة واحدة، يبني قوالبها، يتحقق من التزام المستندات بها، ويجمع حالة كل المشاريع في تقرير واحد.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
