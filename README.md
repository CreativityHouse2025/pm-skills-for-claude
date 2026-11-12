# Project Management Skills for Claude

Open skills that help people run real projects with Claude: build the right document, keep all documents consistent, and review what you have written. English and Arabic.

Created by Creativity House (دار الإبداع).

## Skills

| Skill | What it does | Status |
|---|---|---|
| [`project-companion`](skills/project-companion) | Interviews you about your project, keeps one project fact sheet, builds the next document you need (charter, scope, WBS, schedule, budget, risk register and about 60 more), reviews documents you wrote, and tells you what comes next. Adapts to learners, working project managers, and anyone running a project without project training. | Available |
| [`trainer-toolkit`](skills/trainer-toolkit) | For anyone who teaches project management: builds case studies, class exercises, "spot the mistakes" documents with answer keys, model answers, grading rubrics and complete session packs, and gives rubric-based feedback on a learner's work. | Available |
| [`pmo-kit`](skills/pmo-kit) | For organisations running several projects: writes the organisation's project rules in one standards sheet, then produces its own templates, checks documents against those rules, builds a portfolio status report, sets up prioritisation scoring and stage gates, and writes a handbook for new project managers. | Available |
| [`meeting-to-actions`](skills/meeting-to-actions) | Turns meeting notes or a transcript into decisions, actions with owners and dates, risks and issues, open questions and a ready-to-send follow-up, without inventing owners or dates. | Available |
| [`project-rescue`](skills/project-rescue) | Diagnoses a project in trouble from its own documents, sizes the gap, sets out the real options including reducing scope or stopping, and writes a plain brief for the sponsor. | Available |
| [`ai-governance-companion`](skills/ai-governance-companion) | Helps an organisation govern its AI use: inventory, risk assessment per use, acceptable-use policy, roles, supplier questions, incident process, and a self-assessed gap check with a roadmap. | Available |

## Why this exists

Asking an AI for "a project charter" gives you a template that could belong to any project. These skills fix four gaps:

1. **Generic output** → every document is built from your own project facts, and nothing is invented.
2. **Documents that contradict each other** → one fact sheet feeds every document.
3. **Not knowing what comes next** → each answer names the next useful step.
4. **Nobody to check your work** → reviewing your draft is a main feature.

## Install

**Claude apps (web, desktop, mobile):** download this repository, zip the skill's folder (for example `skills/project-companion`) so that the folder itself is the top level of the ZIP, and upload it in Claude's skills settings. Skills need code execution to be enabled. Current steps: <https://support.claude.com/en/articles/12512180>

**Claude Code:** copy the folder to your personal or project skills directory.

```bash
git clone https://github.com/CreativityHouse2025/pm-skills-for-claude.git
cp -r pm-skills-for-claude/skills/project-companion ~/.claude/skills/
```

Details: <https://code.claude.com/docs/en/skills>

No accounts, API keys or connectors are required. If you have your own tools connected to Claude (a drive, a task tracker), the skill can put documents there when you ask.

## Try it

- "I run a small business and I'm starting a new project. I don't know where to begin."
- "Here is my risk register. Is it good enough for the steering committee?"
- "I'm studying for the PMP. Build a WBS for a project I know and explain it."
- "أحتاج ميثاق مشروع لتطبيق جوال لحجز المواعيد."
- "I teach an intro PM class and have 45 minutes tomorrow for risk registers. Give me a group exercise." (trainer-toolkit)
- "Build one status report for leadership from these four project updates, using our colour rules." (pmo-kit)

## Add a document type

The skill is driven by a catalog, so extending it needs no change to the instructions:

1. Add one row to `skills/project-companion/references/catalog.md` (or `agile.md`).
2. Add its Arabic name to `arabic-terms.md` in the same folder.
3. Optionally add a short block to `review-checklists.md`.
4. Run `python3 tools/sync_shared.py` so the other skills get the same files.

Pull requests are welcome.

## Notes

- These skills describe widely used project management practice in original wording. They are independent and are not affiliated with, endorsed by or official material of any certification body.
- PMI, PMP, CAPM and PMBOK are registered marks of the Project Management Institute, Inc.
- Documents produced are drafts for a competent person to review.

## License

MIT. See [LICENSE](LICENSE).

---

<div dir="rtl">

# مهارات إدارة المشاريع لـ Claude

مهارات مفتوحة تساعدك على إدارة مشروعك الحقيقي مع Claude: إعداد المستند المناسب، والحفاظ على اتساق جميع المستندات، ومراجعة ما كتبته. بالعربية والإنجليزية.

من إعداد دار الإبداع (Creativity House).

## ما الذي تفعله مهارة `project-companion`؟

- تسألك أسئلة قليلة عن مشروعك، وتحفظ إجاباتك في «بطاقة حقائق المشروع».
- تبني المستند التالي الذي تحتاجه (ميثاق المشروع، بيان النطاق، هيكل تجزئة العمل، الجدول الزمني، الموازنة، سجل المخاطر وغيرها) من حقائق مشروعك فقط، دون اختلاق أي معلومة.
- تراجع المستندات التي كتبتها وتحدد النواقص مع صياغة مقترحة.
- تخبرك بالخطوة التالية.
- تتكيف مع المتعلم، ومدير المشاريع الممارس، وكل من يدير مشروعًا دون تدريب متخصص.

## التثبيت

**تطبيقات Claude:** نزّل هذا المستودع، ثم اضغط مجلد `skills/project-companion` في ملف ZIP بحيث يكون المجلد نفسه في أعلى الملف، وارفعه من إعدادات المهارات في Claude. الخطوات الحالية: <https://support.claude.com/en/articles/12512180>

**Claude Code:** انسخ المجلد إلى `~/.claude/skills/`.

لا تحتاج المهارة إلى أي حساب أو ربط خارجي.

## ملاحظات

- هذه المهارات مستقلة وليست مواد رسمية لأي جهة مانحة للشهادات.
- PMI و PMP و CAPM و PMBOK علامات مسجلة لمعهد إدارة المشاريع.
- المستندات الناتجة مسودات يراجعها شخص مختص.

</div>
