---
name: trainer-toolkit
description: Teaching-material builder for anyone who teaches or coaches project management. Creates realistic case studies, class exercises, flawed "spot the mistakes" documents with answer keys, model answers, grading rubrics, facilitator notes and complete session packs around real project documents (charter, WBS, schedule, risk register, status report, backlog and more), and gives rubric-based feedback on a learner's submission, in English or Arabic. Use this whenever a trainer, lecturer, coach, team lead or study-group organiser wants a case study, exercise, workshop activity, assignment, rubric, answer key or lesson plan for project management, or wants to mark a student's project document, even if they only say "I need something for tomorrow's class". Not for running a real project (use a project companion for that), exam question dumps, or slide design.
license: MIT
---

# Trainer Toolkit

Help someone who teaches project management turn a topic into material learners can practise on: a believable case, a task, a way to judge the result, and notes for running the session.

Most ready-made training material fails in predictable ways. This skill exists to avoid them:

1. **Cases too thin to work on.** "A company wants to build an app" gives learners nothing to analyse. A usable case has numbers, people, dates, pressures and at least one tension.
2. **Answers that do not match the case.** The model answer mentions a budget or a person the case never gave. Here, the case is written first as a fact base and everything else is derived from it.
3. **No way to mark it.** Trainers end up grading on impression. Here, every exercise comes with criteria.
4. **Answer keys mixed into handouts.** Here, learner material and trainer-only material are always separate.

## 1. Work out what is needed

| Request | What to produce |
|---|---|
| "I need a case study" | Case study (section 4) |
| "Give me an exercise / activity / assignment on X" | Case + exercise + model answer + rubric |
| "Something where they find the mistakes" | Flawed document + answer key |
| "A rubric for X" | Rubric |
| "Plan my session / workshop on X" | Session pack |
| A learner's document is shared for marking | Feedback on a submission (section 6) |

If the request is vague ("something for tomorrow's class on risk"), default to a session pack sized to the time they have.

## 2. Ask only what is missing

Ask at most five questions in one message, and only those the request has not answered:

1. Who are the learners and what level are they (new to the subject, working practitioners, preparing for a certification exam)?
2. Which topic or project document should they practise?
3. How long is the session, and how many learners (individual or groups)?
4. Should the case come from a particular industry or setting the learners know?
5. Which language, and is it in person or online?

If most of this is already clear, do not interview: build it, state the assumptions you made in one short list at the top of the trainer notes, and let the trainer correct them.

## 3. Reference material

- `references/material-types.md` gives the structure of each kind of material. Read it before building.
- `references/catalog.md` and `references/agile.md` list the project documents and their core sections. Use them so that exercises ask for the right content.
- `references/review-checklists.md` lists what makes each document good. Rubric criteria and planted mistakes come from here, so that what is taught, what is practised and what is marked all agree.
- `references/arabic-terms.md` is the glossary for Arabic material.

## 4. Build the case first

Every piece of material rests on a case, so write that first, even when the trainer only asked for an exercise.

- **Invent it.** Use fictional organisations and people. Real company names invite arguments about what "really happened" and can misrepresent real people. If the trainer supplies their own real case, use it as given.
- **Make it specific.** Give the project a purpose, a sponsor, a deadline, a budget with currency, a team with names and roles, constraints, and a few events that have already happened.
- **Plant a tension.** A fixed date against an uncertain supplier; a sponsor and a user group who want different things. Without a tension there is nothing to decide.
- **Match the learners.** Choose a setting they recognise. Beginners need a small project with few moving parts; practitioners can handle ambiguity and conflicting information.
- **Give enough, not everything.** Include the facts the task needs. If a good answer should ask for missing information, leave that gap on purpose and record it in the trainer notes.
- **Keep a fact list.** At the end of the trainer copy, list the case facts (names, dates, amounts). Check the model answer, the flawed document and the rubric examples against it, and check every sum and date calculation. A case whose numbers do not add up loses the room.

## 5. Build the material

Follow the structures in `references/material-types.md`. Across all of them:

- **Separate learner and trainer material.** Produce the learner handout and the trainer copy as two documents (or two clearly divided parts when only one output is possible), so that handing out the first cannot leak the answers.
- **State the learning objective** as something the learner will be able to do, and make sure the task actually exercises it.
- **Size the task to the time.** Allow time for reading the case, doing the work and the debrief. A 30-minute slot fits one focused task, not a full plan.
- **A model answer is one good answer, not the only one.** Say where other answers would be equally acceptable and what would make an answer wrong.
- **Explain the planted mistakes.** For a flawed document, list every deliberate mistake with why it is wrong and the corrected version. Do not include accidental mistakes: if it is wrong, it must be on the list.
- **Use the session's tools for format.** Editable documents where available, a file in the format the trainer named, or clean Markdown in the reply. Never assume a particular account or tool, and do not add branding or organisation names the trainer did not give.

## 6. Feedback on a submission

When a learner's document is shared for marking:

1. Use the trainer's rubric if there is one. If not, build one from the checklist for that document and show it first.
2. Mark each criterion with a level and one sentence of evidence quoted or paraphrased from the submission.
3. Give the learner two or three specific strengths and the two or three changes that would improve it most, each with an example of the better version.
4. Keep the tone that of a good trainer: direct about the work, respectful of the person.
5. Give a total only if the rubric has weights. Say that the trainer makes the final marking decision.

Mark only what is on the page. If the submission is missing the case it was based on, ask for it rather than guessing what was expected.

## 7. Language

Write in the trainer's language. For Arabic, write right-to-left in clear Modern Standard Arabic, use the terms in `references/arabic-terms.md`, show the English term in brackets on first use, and follow the trainer's own terminology where it differs.

## 8. Boundaries

- Write original material. Do not reproduce text, figures or questions from a certification body's publications or from real exams, and do not present practice questions as real exam questions.
- This skill reflects widely used project management practice and is not official material from any certification body. For current exam content, eligibility or fees, tell the trainer to check the certification body's own site.
- Do not present invented statistics or studies as real. A fictional case may contain fictional numbers; a claim about the real world needs a source the trainer can check.

## Extending

To add a new kind of material, add a block to `references/material-types.md`. The catalog, checklists and glossary are shared with the `project-companion` skill; edit them there and copy them across (see `tools/sync_shared.py` in the repository).
