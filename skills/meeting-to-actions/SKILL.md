---
name: meeting-to-actions
description: Turns meeting notes, transcripts, chat exports or voice-note text into a clear record people can act on - a short summary, decisions, an action list with owners and due dates, risks and issues raised, open questions, and a ready-to-send follow-up message - in English or Arabic. Use this whenever someone shares or pastes notes or a transcript from a meeting, call, workshop, stand-up or site visit and wants minutes, a summary, action items, "who is doing what", a follow-up email, or updates for their risk and issue logs, and whenever they ask what was agreed in a meeting or want to check progress on last meeting's actions, even if they only say "clean these notes up". Not for writing a meeting agenda from scratch, transcribing audio, or summarising documents that are not meeting records.
license: MIT
---

# Meeting to Actions

Turn what was said in a meeting into a record people can act on, without adding anything that was not said.

Meetings fail after they end. Notes are long, decisions are buried, and "someone should look into that" never gets an owner. A plain summary makes this worse in three ways, which this skill is built to avoid:

1. **It invents tidy endings.** A summary that assigns an owner or a date nobody agreed creates false commitments. Here, a gap stays visible as a gap.
2. **It blurs decisions with discussion.** "We talked about moving the launch" is not "we decided to move the launch". Here, they are separated.
3. **It stops at the summary.** The useful output is the action list, the log updates and the follow-up message.

## 1. What to produce

Default to the **standard record** below. Switch when the request points elsewhere.

| Request | Output |
|---|---|
| "Summarise / clean up these notes", or just a pasted transcript | Standard record |
| "Just the actions" | Action list and items needing confirmation only |
| "Formal minutes" | Formal minutes (see section 4) |
| "Write the follow-up" | Follow-up message, built from the standard record |
| Previous actions supplied with new notes | Standard record plus an action follow-up table |

### Standard record

1. **Header**: meeting name, date, attendees, as given. Leave out what was not given; do not guess attendees from names mentioned.
2. **Summary**: three to five lines on what the meeting was for and where it ended.
3. **Decisions**: each decision in one line, with who made it when that is clear.
4. **Actions**: a table of action, owner, due date, and a short note on where it came from.
5. **Risks and issues raised**: things that might go wrong (risks) and things that already have (issues), each worded so it can be pasted into a log.
6. **Open questions and parked items**: what was raised and not settled.
7. **Needs confirming**: every action without an owner or date, every unclear decision, anything you could not attribute.

Leave out a section that has nothing in it, except Needs confirming: if that is empty, say so in one line, because it tells the reader the record is complete.

## 2. Rules for reading the meeting

- **Record only what was said.** Do not add owners, dates, numbers or decisions. Write `Owner: not assigned` or `Due: not set` and list the item under Needs confirming.
- **Classify carefully.** A decision needs agreement or a clear call by someone with authority. A proposal nobody answered is an open question. "I'll try to look at it" is a tentative action: record it with that wording.
- **Write actions that can be done.** Start with a verb, name the thing, keep the speaker's meaning. "Sara to send the revised quote to the client" beats "Quote".
- **Handle dates with care.** Convert "next Friday" to a calendar date only when the meeting date is known, and show both. Otherwise keep the words as said.
- **Attribute only when clear.** If the notes do not show who said or agreed something, say so. Do not assign by guessing from job titles.
- **Keep disagreement neutral.** State each position in a line without judging it.
- **Leave out the personal.** Side chatter, jokes, and remarks about a person's performance or private life stay out of the record, even if they are in the transcript.
- **Read all of it.** With a long transcript, late reversals matter: if a decision made early is changed later, record the final position and note the change.
- **Flag contradictions** inside the notes, or between the notes and any plan, fact sheet or log supplied, instead of silently choosing one.

## 3. Connecting to the project

When the person supplies a project fact sheet, risk register, issue log or previous action list:

- Use the same names, IDs and date format.
- Number new risks and issues by continuing the existing sequence, and mark them `NEW`. If a raised item matches an existing entry, show it as an update to that entry.
- For previous actions, produce a follow-up table: action, owner, original due date, status (done, in progress, not started, not mentioned), and the evidence from this meeting. `Not mentioned` is a status of its own; do not assume it is done.
- List which project documents now need updating because of what was decided.

Without those inputs, give the risks and issues as plain statements and do not invent IDs.

## 4. Formats

**Follow-up message.** Short and ready to send: one line of thanks or context, decisions, actions grouped by owner with dates, items needing confirmation phrased as questions to named people, next meeting if stated. Match the register of the meeting: a team chat message for a stand-up, an email for a client meeting. Do not send it; give it to the person. Send or post only when they ask and have a tool connected for it.

**Formal minutes.** Title, date, time and place, present and apologies, then numbered items: discussion in brief, decision, action with owner and date. Close with the next meeting and a line for approval. Neutral, past tense.

**Tasks in a tracker.** If the person has a task tool connected and asks for the actions to be created there, show the list first and confirm before creating them, since bulk-created tasks with wrong owners are tedious to undo.

## 5. Language

Write in the language the person uses with you, even when the meeting was in another language or mixed two. Keep names, product terms and quoted phrases as spoken. For Arabic, write right-to-left in clear Modern Standard Arabic and keep dates and numbers in one format.

## 6. Boundaries

- This skill works from text. If given only an audio file and no transcription tool is available, say that a transcript is needed.
- A record made from partial notes is partial. Say so when the notes are clearly incomplete (they start mid-discussion, or reference decisions that are not in them).
- Minutes with legal weight (board meetings, disciplinary or contractual meetings) are drafts for the responsible person to check and approve.
