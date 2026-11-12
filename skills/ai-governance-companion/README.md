# AI Governance Companion

Practical, proportionate rules for using AI in your organisation.

A skill for Claude. Part of [Project Management Skills for Claude](../../README.md), created by Creativity House.

## What it does

- Builds an inventory of where AI is used, by use and not by tool
- Assesses each use for risk and proposes controls
- Drafts an acceptable-use policy staff will actually read
- Defines roles, supplier questions and an incident process
- Runs a self-assessed gap check against a framework you choose and turns it into a roadmap

## Who it is for

Compliance and operations leads, IT managers, business owners whose staff use AI tools.

## Try it

- "Staff use AI tools and we have no rules. A client is asking about our AI policy. Help."
- "Is using AI to screen CVs risky? What controls do we need?"
- "How far are we from an AI management system standard?"

Works in English and Arabic. No accounts, API keys or connectors are required.

## What you can rely on

- Not legal advice, an audit or a certification
- Requirements of laws and standards are looked up and attributed, not stated from memory
- Never invents your organisation's AI uses or controls

## Install

**Claude apps:** zip this folder so that `ai-governance-companion` is the top level of the ZIP (or download the ready-made ZIP from the repository's Releases page) and upload it in Claude's skills settings. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy this folder to `~/.claude/skills/` or to your project's `.claude/skills/`.

## What is in this folder

- `SKILL.md`: the instructions Claude follows
- `assets/`
  - `governance-sheet.md`
- `evals/`
  - `agency-client-questionnaire/`
  - `gap-check-is-self-assessment/`
  - `refuses-to-invent-inventory-arabic/`
- `references/`
  - `frameworks.md`
  - `outputs.md`
- `README.md`, `LICENSE`: this page and the licence

`evals/` holds 3 test cases. Each has a prompt, the expected outcome and the checks a good answer must pass.

## Status

Version 0.1.0, pre-release. See the [changelog](../../CHANGELOG.md). Problems and suggestions are welcome through the repository's issues.

## Licence

MIT. See [LICENSE](LICENSE).

---

<div dir="rtl">

## بالعربية

لحوكمة استخدام الذكاء الاصطناعي في المؤسسة: سجل الاستخدامات، تقييم المخاطر لكل استخدام، سياسة استخدام مقبول، الأدوار، أسئلة للمورّدين، وخطة لسد الفجوات.

تعمل المهارة بالعربية والإنجليزية ولا تحتاج إلى أي حساب أو ربط خارجي. للتثبيت: ارفع مجلد المهارة مضغوطًا من إعدادات المهارات في Claude.

</div>
