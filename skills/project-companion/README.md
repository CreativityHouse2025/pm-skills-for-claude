# Project Companion

A project assistant that works from your real project.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Learns your project once and keeps it in a one-page project fact sheet
- Builds the document you need next from your own facts (64 documents, from charter to closure report, plus agile)
- Reviews documents you wrote: verdict, gaps in order of seriousness, suggested rewording
- Names the single most useful next step after every answer
- Adapts to learners, practitioners and people with no project training

## Who it is for

Business owners, managers, project managers, students, freelancers, event organisers.

## Try it

- "I manage a dental clinic and want to move bookings from paper to a system in two months. Where do I start?"
- "Here is my risk register. Is it good enough for the steering committee?"
- "I'm studying for the PMP. Build a WBS for a career fair and explain it."

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Never invents budgets, dates or names; gaps become open questions or labelled assumptions
- Charts that need real measurements are built only from numbers you supply
- Documents are drafts for a competent person to review

## Install

**Claude apps:** zip this folder so that `project-companion` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `assets/`
  - `project-fact-sheet.md`
- `evals/`
  - `everyday-first-document-arabic/`
  - `learner-wbs-explained/`
  - `practitioner-risk-register-review/`
- `references/`
  - `agile.md`
  - `arabic-terms.md`
  - `catalog.md`
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

مساعد لإدارة مشروعك الحقيقي: يسألك أسئلة قليلة، يحفظ حقائق المشروع في بطاقة واحدة، يبني المستند التالي الذي تحتاجه، يراجع مستنداتك، ويخبرك بالخطوة التالية.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
