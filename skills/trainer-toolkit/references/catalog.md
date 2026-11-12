# Deliverables catalog

One row per document. **Tier**: `core` = the small set almost every project needs (the only set offered to people without project training); `standard` = typical for a managed project; `extended` = large, formal or regulated projects. **Builds on** lists IDs that should exist first; if they do not, build from the fact sheet and say what was skipped.

Updating an existing document (risk register, issue log, plan) is an edit to that document with a new version number, not a new document.

## Contents
- Initiating (I)
- Planning (P)
- Executing (E)
- Monitoring and controlling (M)
- Closing (C)

## Initiating

| ID | Document | What it settles | Core sections | Format | Builds on | Tier |
|---|---|---|---|---|---|---|
| I-01 | Business case | Whether the project deserves money and attention | Problem or opportunity; options considered (including doing nothing); recommended option; costs and expected benefits; strategic fit; main risks; how success will be measured | Document | - | standard |
| I-02 | Feasibility study | Whether the project can realistically be done | Technical, operational, financial and legal feasibility; findings; risks; recommendation | Document | - | extended |
| I-03 | Project charter | That the project exists, why, and who has authority to run it | Purpose; measurable objectives; high-level scope and exclusions; key deliverables; milestones; budget summary; high-level risks; assumptions and constraints; key stakeholders; project manager and authority level; sponsor; approval | Document | I-01 if one exists | core |
| I-04 | Stakeholder register | Who is affected and how to work with each of them | Name or group; role; interest; influence; expectations; engagement approach; communication needs | Sheet | I-03 | core |
| I-05 | Assumptions and constraints log | What is being taken as true and what limits the project | ID; statement; type (assumption or constraint); owner; date to confirm; status | Sheet | I-03 | standard |

## Planning

| ID | Document | What it settles | Core sections | Format | Builds on | Tier |
|---|---|---|---|---|---|---|
| P-01 | Project management plan | How the project will be run and controlled | Life cycle and approach; summary of scope, schedule and cost baselines; how each area is managed (short sections or links to subsidiary plans); governance; change control | Document | I-03 | standard |
| P-02 | Scope management plan | How scope will be defined, checked and controlled | Process for defining scope; acceptance process; how scope changes are handled; roles | Document | I-03 | extended |
| P-03 | Scope statement | Exactly what is and is not included | Objectives; deliverables with acceptance criteria; in scope; out of scope; assumptions; constraints | Document | I-03 | core |
| P-04 | Requirements traceability matrix | That every requirement leads to a deliverable and a test | Requirement ID; description; source; priority; linked deliverable or WBS code; verification method; status | Sheet | P-03 | standard |
| P-05 | Work breakdown structure (WBS) | All the work, broken into manageable pieces | Hierarchy from project to deliverables to work packages; WBS codes; short dictionary entry for key work packages (description, owner, acceptance) | Outline or sheet | P-03 | core |
| P-06 | Schedule management plan | How the schedule will be built, tracked and changed | Scheduling method and tool; level of detail; update frequency; variance thresholds; roles | Document | P-01 | extended |
| P-07 | Activity list and sequence | What tasks exist and in what order | Activity ID; WBS code; description; predecessors; dependency type; duration estimate and basis; owner | Sheet | P-05 | standard |
| P-08 | Network diagram | How activities depend on each other | Nodes for activities; dependency arrows; critical path marked | Diagram | P-07 | extended |
| P-09 | Project schedule | When everything happens | Tasks with start and finish dates; dependencies; milestones; owners; critical path noted; Gantt view where the tool allows | Sheet | P-05 | core |
| P-10 | Milestone list | The key checkpoints | Milestone; target date; what must be true to call it done; owner | Sheet | P-09 | standard |
| P-11 | Cost management plan | How costs will be estimated, budgeted and controlled | Estimating method; units and precision; reporting format; variance thresholds; roles | Document | P-01 | extended |
| P-12 | Cost estimate and budget | What it will cost and when the money is needed | Cost per work package or category; basis of estimate; contingency reserve; total budget; spend by period | Sheet | P-05 | core |
| P-13 | Baselines (scope, schedule, cost) | The approved versions that progress is measured against | Approved scope statement and WBS; approved schedule; approved time-phased budget; approval date and approver | Document plus sheets | P-03, P-09, P-12 | standard |
| P-14 | Risk management plan | How risks will be found, rated and handled | Approach; roles; probability and impact scales; scoring matrix; review frequency; reporting | Document | P-01 | standard |
| P-15 | Risk register | What could go wrong or right, and what will be done about it | ID; risk statement (cause, event, effect); category; probability; impact; score; response strategy; actions; owner; trigger; status | Sheet | I-03 | core |
| P-16 | Resource plan | Who and what is needed, and when | Role or resource; quantity; skills; source; dates needed; cost rate where known | Sheet | P-05 | standard |
| P-17 | Responsibility matrix (RACI) | Who does, decides, advises and is kept informed | Activities or deliverables down the side; people or roles across the top; R, A, C, I in each cell; exactly one A per row | Sheet | P-05 or I-03 | core |
| P-18 | Communications plan | Who needs what information, when and how | Audience; information; purpose; frequency; channel; owner | Sheet | I-04 | core |
| P-19 | Quality management plan | What "good enough" means and how it will be checked | Quality standards; metrics and targets; assurance activities; control checks; roles | Document | P-03 | standard |
| P-20 | Procurement plan | What will be bought and how suppliers are chosen and managed | Items to procure; make-or-buy reasoning; contract types; selection criteria; timeline; procurement risks | Document | P-03 | standard |
| P-21 | Stakeholder engagement plan | How to move each key stakeholder to the support the project needs | Stakeholder; current and desired engagement level; actions; owner; timing | Sheet | I-04 | standard |
| P-22 | Change management plan | How changes are requested, assessed and approved | Request process; impact assessment; approval levels; who decides; how approved changes are communicated | Document | P-01 | standard |

## Executing

| ID | Document | What it settles | Core sections | Format | Builds on | Tier |
|---|---|---|---|---|---|---|
| E-01 | Status report | Where the project stands right now | Period; overall status; progress against milestones; work done; work planned; top risks and issues; decisions needed; budget status | Document | P-09 | core |
| E-02 | Issue log | Problems that have already happened and who is fixing them | ID; description; date raised; impact; priority; owner; action; target date; status | Sheet | - | core |
| E-03 | Change request | Whether a specific change should be approved | Change description; reason; impact on scope, schedule, cost, quality and risk; options; recommendation; decision and approver | Document | P-03 | core |
| E-04 | Decision log | What was decided, by whom and why | ID; decision; rationale; decided by; date; follow-up status | Sheet | - | standard |
| E-05 | Meeting summary and action items | What a meeting agreed and who does what next | Date and attendees; decisions; action items with owner and due date; open points | Document | - | core |
| E-06 | Team assignments | Who is working on what in the current period | Person; role; assigned work packages or tasks; dates; allocation | Sheet | P-16 or P-17 | extended |
| E-07 | Quality assurance report | Whether the work is following the agreed quality process | Scope of review; findings; non-conformities; corrective actions; owner | Document | P-19 | extended |
| E-08 | Team performance report | How the team is performing and what would help | Period; achievements; measures used; obstacles; improvement actions | Document | - | extended |
| E-09 | Contracts and service-level tracker | Whether suppliers are meeting their obligations | Supplier; contract; key terms and service levels; compliance status; renewal or end date; owner | Sheet | P-20 | extended |
| E-10 | Lessons learned register | What to repeat and what to avoid, captured while it is fresh | ID; date; situation; what happened; lesson; recommendation; owner | Sheet | - | standard |

## Monitoring and controlling

| ID | Document | What it settles | Core sections | Format | Builds on | Tier |
|---|---|---|---|---|---|---|
| M-01 | Performance report | How actual progress compares with the baselines | Scope, schedule and cost against baseline; variances and causes; forecast; corrective actions. Earned value figures only when planned value, earned value and actual cost are provided | Document | P-13 | standard |
| M-02 | Risk review | Whether the risk picture has changed | Risks closed; new risks; changed scores; response progress; triggers reached (applied as an update to P-15) | Sheet update | P-15 | standard |
| M-03 | Change log | The status of every change request | ID; change; requested by; date; decision (approved, rejected, pending); impact summary; implementation status | Sheet | E-03 | standard |
| M-04 | Quality control measurements | Whether deliverables meet their acceptance criteria | Deliverable; criterion; measurement; result; pass or fail; action | Sheet | P-19 | extended |
| M-05 | Plan update | That the plan reflects approved changes | What changed; which sections and baselines were revised; version; approver (applied as an update to P-01) | Document update | P-01, M-03 | extended |

## Closing

| ID | Document | What it settles | Core sections | Format | Builds on | Tier |
|---|---|---|---|---|---|---|
| C-01 | Handover and transition plan | How the result passes to the people who will use and support it | What is handed over; to whom; training and documentation; support arrangements; outstanding items; acceptance | Document | P-03 | core |
| C-02 | Project closure report | How the project performed overall | Objectives against results; scope, schedule and cost performance; benefits so far; open items; acknowledgements | Document | I-03 | core |
| C-03 | Final lessons learned | What the organisation should carry into future projects | What went well; what was hard; root causes; recommendations, each with an owner | Document | E-10 if one exists | core |
| C-04 | Contract closure record | That supplier agreements are complete and settled | Contract; deliverables accepted; payments settled; claims closed; date and sign-off | Sheet | P-20 | standard |
| C-05 | Formal acceptance record | That the customer or sponsor accepts the result | Deliverables accepted; acceptance criteria met; exceptions; signatures and date | Document | P-03 | standard |
| C-06 | Final financial report | How spending compared with budget | Budget; actual cost; variances and reasons; remaining commitments | Sheet | P-12 | standard |
| C-07 | Post-implementation review | Whether the benefits actually appeared after go-live | Benefits expected against realised; user feedback; issues since go-live; recommendations | Document | C-02 | extended |
| C-08 | Customer satisfaction survey | How the customer and stakeholders rate the result and the delivery | Questions on delivery, quality, communication and expectations; rating scale; open comments | Form | - | extended |
