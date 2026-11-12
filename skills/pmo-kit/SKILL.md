---
name: pmo-kit
description: Project standards and portfolio toolkit for any organisation running more than one project. Captures how the organisation runs projects in one standards sheet (project sizes, required documents, approval levels, status colour rules, risk scales, naming, reporting rhythm), then produces the organisation's own template set, checks a project document against those house rules, builds a portfolio status report across projects, sets up project intake and prioritisation scoring, defines stage gates, and writes a "how we run projects here" handbook, in English or Arabic. Use this whenever someone manages or oversees several projects, is setting up a PMO, wants consistent templates across teams, asks which project documents their company should require, needs a combined status report for leadership, or wants to prioritise project requests, even if they never say "PMO" or "portfolio". Not for building a single project's documents from scratch (use a project companion for that) or for teaching material.
license: MIT
---

# PMO Kit

Help an organisation run its projects the same way every time, and see all of them on one page.

A single project needs good documents. An organisation with ten projects has a different problem:

1. **Every team does it differently.** One status report says "green" meaning "no one has complained", another means "within 5% of plan". Leadership cannot compare them.
2. **Nobody knows what is required.** Small projects drown in paperwork while large ones skip approvals.
3. **There is no combined view.** Leaders read ten reports and still cannot say which three projects need them this week.
4. **Priorities are set by whoever asks loudest.**

This skill fixes those by writing the organisation's rules down once and applying them everywhere.

## 1. Work out what is being asked

| Request | What to do |
|---|---|
| "Help us standardise / set up a PMO" | Build the standards sheet (section 2), then the template set |
| "Make our templates" | Template set (needs the standards sheet) |
| "Does this document follow our process?" | Compliance check |
| "Give me one report across our projects" | Portfolio status report |
| "Which projects should we do first?" | Intake and prioritisation |
| "What approvals should a project pass?" | Stage gates |
| "Write this up for new project managers" | Handbook |

Structures for each output are in `references/outputs.md`. Read the relevant block before building.

## 2. The standards sheet

The standards sheet is the organisation's rule book in one page, and everything else is derived from it. Use the template in `assets/standards-sheet.md`.

**If one exists** (pasted, attached, earlier in the conversation), use it and do not re-ask.

**If not**, interview briefly. Ask at most six questions in one message, only those not already answered:

1. What kind of organisation is this, and roughly how many projects run at once?
2. How do your projects differ in size (budget, duration, team)? Where would you draw the line between small, medium and large?
3. Who approves a project, and does that change with size or cost?
4. What do leaders want to see regularly, and how often?
5. Which documents do teams already produce, and which cause complaints?
6. Is there existing terminology, numbering or branding to keep?

**The rules belong to the organisation, not to you.** Where they have no rule yet, propose a sensible default and label it `SUGGESTED, needs approval`, so that a draft is never mistaken for agreed policy. Typical suggestions: three project sizes; status colours tied to stated thresholds; a five-level probability and impact scale; a monthly portfolio review. Keep suggestions proportionate: a twelve-person company does not need five stage gates.

When rules are confirmed, change the label to `AGREED` with the date and who agreed. Give the updated sheet back as a file each time it changes, and tell the person to bring it to future conversations.

## 3. Required documents by size

Use `references/catalog.md` (and `references/agile.md` for iterative teams) as the menu. For each project size in the standards sheet, list which documents are required, optional or not needed. Start from the catalog tiers (`core` for small, plus `standard` for medium, plus `extended` for large) and adjust to what the organisation says. Fewer required documents that people actually keep up to date beat a long list that is ignored.

## 4. Building from the standards

- **Templates** carry the organisation's rules inside them: the ID format, the approval block with the right approver for that size, the organisation's own scales and colour definitions, and a short guidance note per section saying what a good entry looks like. Guidance notes are marked so they can be deleted.
- **Compliance checks** compare a document with the standards sheet first (is it the right template, are required sections and approvals present, do IDs and scales follow the rules) and with good practice second (`references/review-checklists.md`). Report the two separately, because "not our format" and "not a good risk statement" call for different fixes.
- **Branding** is applied only from what the person provides (name, colours, logo placement, footer text). Never invent a logo, a slogan or contact details.
- **Format** follows what the session offers: editable documents and sheets where available, a file in the format they named, or Markdown in the reply. If the person has their own tools connected (a drive, a tracker) and asks for output there, or asks you to read project data from there, use them; never assume a particular account or tool.

## 5. Portfolio reporting

A portfolio report is only as trustworthy as its inputs, so be strict about them.

- **Use only supplied data.** Each project's status, dates, spend and risks come from its fact sheet, status report or tracker export. Never fill a gap with a guess; show `Not reported` and list what is missing and from whom.
- **Apply the organisation's colour rules, not the project manager's own label.** If a project reports "green" but its numbers meet the amber or red rule, show the rule-based colour and note the difference. If no rule exists yet, show the reported colour, say it is self-reported, and suggest a rule.
- **Flag stale inputs.** If a report is older than the reporting rhythm in the standards sheet, mark it stale.
- **Calculate, do not estimate.** Totals, variances and percentages are computed from the figures given (run the arithmetic in code when a code tool is available) and shown with their inputs.
- **Lead with what needs a decision.** The first section is the short list of projects that need leadership action, with the decision required. The full table comes after.
- **Report on projects, not on people.** Describe delays and causes in terms of the work and conditions, not individual performance.

## 6. Prioritisation

Scores come from the organisation's criteria, weights and ratings. Help them choose criteria and weights, then calculate. Do not rate a project on their behalf: if a rating is missing, ask, or show the ranking with that project marked incomplete. Always show the working so the ranking can be challenged, and say plainly that the score informs the decision and does not make it.

## 7. Language

Write in the person's language. For Arabic, write right-to-left in clear Modern Standard Arabic, use `references/arabic-terms.md`, show the English term in brackets on first use, and follow the organisation's own terms where they differ.

## 8. Boundaries

- This skill reflects widely used project and portfolio management practice and is not official material from any standards or certification body.
- Policies with legal, financial-control, safety or employment effects (delegated spending authority, contract approvals) are drafts for the organisation's own authorised people to review.
- Do not present a `SUGGESTED` rule as the organisation's policy in anything addressed to leadership or staff; show the label.

## Extending

Add a new kind of output as a block in `references/outputs.md`. The catalog, checklists and glossary are shared with the `project-companion` skill; edit them there and copy them across (see `tools/sync_shared.py` in the repository).
