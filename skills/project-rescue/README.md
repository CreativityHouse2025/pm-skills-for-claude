# Project Rescue

An honest diagnosis and recovery plan for a project in trouble.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Separates symptoms from root causes, using your project's own documents
- Calculates the gap in time, cost and scope, and shows the working
- Sets out the real options: recover, reduce scope, add time or money, pause and re-plan, stop
- Builds a recovery plan with first-two-week actions and early warning signs
- Writes a one-page brief for the sponsor

## Who it is for

Project managers and business owners whose project is late, over budget, stuck, or newly inherited.

## Try it

- "I took over a project that has spent 87% of its budget with 40% of the features done. What do I do?"
- "Management says we must continue because we've spent so much. What do you think?"
- "Help me tell the sponsor the real position."

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Findings without evidence are labelled as hypotheses
- Does not blame individuals, and will not help make status look better than it is
- Contract, legal and HR questions are flagged for the right people

## Install

**Claude apps:** zip this folder so that `project-rescue` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `evals/`
  - `inherited-app-over-budget/`
  - `sunk-cost-arabic/`
  - `vague-distress-asks-first/`
- `references/`
  - `diagnostic.md`
- `README.md`, `LICENSE`: this page and the licence

`evals/` holds 3 test cases. Each has a prompt, the expected outcome and the checks a good answer must pass.

## Status

Version 0.1.0, pre-release. See the [changelog](../../CHANGELOG.md). Problems and suggestions are welcome through the repository's issues.

## Licence

MIT. See [LICENSE](LICENSE).

---

<div dir="rtl">

## بالعربية

لتشخيص مشروع متعثر: يفرّق بين الأعراض والأسباب، يحسب حجم الفجوة في الوقت والتكلفة والنطاق، يعرض الخيارات الواقعية، ويكتب ملخصًا صريحًا لراعي المشروع.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
