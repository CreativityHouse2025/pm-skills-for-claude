# Trainer Toolkit

Practice material for anyone who teaches project management.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Writes realistic, invented case studies with names, dates, budgets and a built-in tension
- Builds exercises sized to your session: build, spot the mistakes, improve, decide, role-play
- Produces flawed documents with a full answer key
- Creates model answers, grading rubrics, facilitator notes and complete session packs
- Gives rubric-based feedback on a learner's submission

## Who it is for

Trainers, lecturers, coaches, team leads who run workshops, study-group organisers.

## Try it

- "I have 45 minutes tomorrow for risk registers with 18 beginners. Give me a group exercise."
- "I need a project charter with deliberate mistakes and an answer key."
- "Mark this student's WBS. I don't have a rubric."

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Learner handouts and trainer-only material are always separate
- Original material only; nothing copied from certification bodies or real exams
- Does not design slides

## Install

**Claude apps:** zip this folder so that `trainer-toolkit` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `evals/`
  - `flawed-charter-arabic/`
  - `mark-submission-wbs/`
  - `session-pack-risk-beginners/`
- `references/`
  - `agile.md`
  - `arabic-terms.md`
  - `catalog.md`
  - `material-types.md`
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

أدوات للمدرّب: دراسات حالة، تمارين، مستندات فيها أخطاء مقصودة مع مفتاح الإجابة، إجابات نموذجية، معايير تقييم، وخطط جلسات كاملة.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
