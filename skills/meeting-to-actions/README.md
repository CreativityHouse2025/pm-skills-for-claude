# Meeting to Actions

From meeting notes to a record people can act on.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Separates decisions from discussion
- Lists actions with owner and due date, exactly as agreed
- Captures risks and issues raised, ready for your logs
- Lists open questions and everything that still needs confirming
- Writes a ready-to-send follow-up message
- Tracks last meeting's actions: done, in progress, or not mentioned

## Who it is for

Anyone who runs or attends meetings: project managers, team leads, account managers, coordinators.

## Try it

- "Turn these call notes into something I can send round."
- "Here are last week's actions and today's stand-up notes. Where are we?"
- "Write formal minutes from this transcript."

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Never invents an owner, a date or a decision that was not stated
- Works from text; audio needs a transcript first
- Minutes with legal weight are drafts for the responsible person to approve

## Install

**Claude apps:** zip this folder so that `meeting-to-actions` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `evals/`
  - `arabic-output-from-english-notes/`
  - `follow-up-on-previous-actions/`
  - `messy-client-call-notes/`
- `README.md`, `LICENSE`: this page and the licence

`evals/` holds 3 test cases. Each has a prompt, the expected outcome and the checks a good answer must pass.

## Status

Version 0.1.0, pre-release. See the [changelog](../../CHANGELOG.md). Problems and suggestions are welcome through the repository's issues.

## Licence

MIT. See [LICENSE](LICENSE).

---

<div dir="rtl">

## بالعربية

يحوّل ملاحظات الاجتماع إلى قرارات، ومهام بمسؤول وتاريخ، ومخاطر وإشكالات، وأسئلة مفتوحة، ورسالة متابعة جاهزة للإرسال، دون اختلاق أي تفصيل.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
