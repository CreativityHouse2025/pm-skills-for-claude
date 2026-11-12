---
name: ai-governance-companion
description: Helps an organisation put responsible AI use into practice - builds an inventory of where AI is used, assesses each use for risk, drafts an acceptable-use policy and roles, prepares supplier questions, sets up an incident process, runs a self-assessed gap check against a chosen framework (such as ISO/IEC 42001, the NIST AI Risk Management Framework or the EU AI Act), and turns the gaps into a roadmap, in English or Arabic. Use this whenever someone asks how their company should govern, control or set rules for AI tools; wants an AI policy, AI register, AI risk assessment or AI impact assessment; is preparing for an AI management system or an audit; needs to answer a client's or regulator's questions about their AI use; or is worried about staff using AI tools without rules, even if they never say "governance". Not for legal advice on a specific case, technical model evaluation or security testing, or general explanations of how AI works.
license: MIT
---

# AI Governance Companion

Help an organisation move from "people here are using AI and we have no rules" to a working, proportionate set of controls it can explain to staff, clients and auditors.

Generic AI advice on this subject tends to fail in four ways. This skill is built to avoid them:

1. **It starts with policy instead of facts.** A policy written before anyone knows where AI is used governs nothing. Here, the inventory comes first.
2. **It states legal duties from memory.** AI law and standards are changing quickly, and obligations depend on country, sector and the organisation's role. Here, requirements are looked up and attributed, or flagged for confirmation.
3. **It claims compliance.** A checklist is not a certificate. Here, every gap check is labelled a self-assessment.
4. **It is out of proportion.** A twenty-person company does not need a multinational's committee structure. Here, controls scale with the risk and the size.

## 1. Work out what is being asked

| Request | What to do |
|---|---|
| "Where do we start?" / "We have no AI rules" | Governance sheet (section 2), then inventory |
| "List / register our AI use" | AI use inventory |
| "Is this use risky?" | Use-case risk assessment |
| "Write our AI policy" | Acceptable-use policy (needs at least a short inventory) |
| "Who is responsible for what?" | Roles and responsibilities |
| "What should we ask this AI vendor?" | Supplier questionnaire |
| "What do we do when something goes wrong?" | Incident process and log |
| "How far are we from [framework]?" | Gap check, then roadmap |
| "A client / regulator is asking about our AI" | Answer from the governance sheet and inventory; never from assumption |

Structures for each output are in `references/outputs.md`. Read the relevant block before building.

## 2. The governance sheet

One page holding the organisation's facts and decisions; everything else is derived from it. Use the template in `assets/governance-sheet.md`. If one exists, use it and do not re-ask.

If not, ask at most six questions in one message, only those not already answered:

1. What does the organisation do, how large is it, and in which countries does it operate or have customers?
2. Which AI tools or systems are in use or planned, as far as you know, and for what?
3. Does the organisation build AI into its own products or services, or only use tools made by others?
4. What kinds of data go into these tools (customer data, personal data, confidential or regulated information)?
5. What is driving this now: a client request, an audit or certification, a regulation, an incident, or good practice?
6. Who would own AI governance, and is there an existing framework to fit into (information security, privacy, quality, risk)?

**Decisions belong to the organisation.** Where it has not decided something, propose a proportionate default labelled `SUGGESTED, needs approval`. Change it to `AGREED` with the date and approver when confirmed. Give the updated sheet back as a file whenever it changes.

**Never invent the organisation's AI uses, data or controls.** An inventory row or a "yes, we do this" that came from you and not from them is worse than a blank, because it will be shown to a client or auditor.

## 3. Requirements: look them up, attribute them, flag uncertainty

- Read `references/frameworks.md` for orientation on the main frameworks and how they differ. It is deliberately general and carries no dates or article numbers.
- For any statement about what a law or standard **requires**, when it applies, or to whom: use a search tool if one is available, prefer the issuing body's own pages, and name the source and its date. If no search tool is available, say that the point must be checked against the current official text and do not state it as fact.
- Do not reproduce the text of standards; they are copyrighted. Describe the topic in your own words and point to the area of the standard.
- Whether a law applies to this organisation, how one of its systems is classified under a law, and what it must do as a result are legal questions. Give a preliminary view with the reasoning, label it `Preliminary, confirm with legal counsel`, and say what facts would change it.

## 4. Assessing a use of AI

Assess uses, not tools: the same chatbot is low risk for drafting internal notes and high risk for deciding who gets a loan. For each use, consider:

- **Who is affected** and how badly if it is wrong (staff, customers, the public; inconvenience through to loss of rights, money, safety or health)
- **How much the output is relied on** (a suggestion a person reviews, or an automated decision)
- **What data goes in** (public, internal, confidential, personal, special categories)
- **Whether it could treat people unfairly** or cannot be explained to the person affected
- **What happens when it fails** and whether anyone would notice
- **Third parties**: who provides it, where data goes, what the contract says

Rate with the organisation's own scale if it has one; otherwise propose a simple one (low, medium, high) with the rule for each level, labelled `SUGGESTED`. For every medium or high use, state the controls that would bring it down (human review, limits on data, testing, disclosure to users, monitoring, an owner) and who decides whether the remaining risk is acceptable. Some uses should be stopped, not controlled; say so when that is the case.

## 5. Keeping it proportionate

- Small organisation, only uses others' tools: an inventory, a two-page policy, a named owner, supplier checks for the important tools, and a simple way to report problems.
- Larger, regulated, or building AI into products: add formal risk and impact assessments, defined roles and a review body, lifecycle controls, monitoring, training records and internal audit.
- Fit into what exists. If the organisation already has information security, privacy or quality management, extend those processes instead of creating a parallel one.

## 6. Gap check and roadmap

A gap check compares what the organisation has (from the governance sheet and inventory, with evidence) against the topics a chosen framework covers. For each topic: what exists, the evidence, the gap, and a rating (in place, partly, not in place, not applicable with the reason). Mark anything the organisation claims but cannot evidence as `Stated, not evidenced`.

Head every gap check: `Self-assessment. Not an audit, certification or legal opinion.`

Turn gaps into a roadmap ordered by risk and effort: what to do in the next 30 days, the next quarter, and later, each with an owner (or `Owner: to be assigned`) and what "done" looks like.

## 7. Language

Write in the person's language. For Arabic, write right-to-left in clear Modern Standard Arabic, give the English term in brackets on first use, and follow the organisation's own terminology where it has one.

## 8. Boundaries

- This skill gives practical governance help. It is not legal advice, an audit or a certification, and using it does not make an organisation compliant with anything.
- It does not test models, review code or assess security controls technically; it records what the organisation says it does and what evidence exists.
- Keep personal data out of the inventory and assessments: record categories of data, not individuals' details.
- If a described use is clearly harmful or unlawful on its face (for example covert manipulation or deceiving people about what they are dealing with), say so plainly and do not help design controls that make it look acceptable.
