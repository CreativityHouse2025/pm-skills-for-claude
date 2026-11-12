# Contributing

Thank you for helping improve these skills. Reports from real use are the most valuable contribution.

## Report a problem

Open an issue and include:
- which skill
- the message you sent (remove anything confidential)
- what the skill did, and what you expected instead

## Suggest a change

1. Fork the repository and create a branch (`fix/...` or `feat/...`).
2. Make the change in the skill's folder under `skills/`.
3. If you changed the catalog, review checklists, agile list or Arabic terms, edit them in `skills/project-companion/references/` and run `python3 tools/sync_shared.py`. Do not edit the copies in other skills.
4. Add or update a test case in the skill's `evals/` folder that shows the behaviour you changed.
5. Add a line to `CHANGELOG.md` under an "Unreleased" heading.
6. Open a pull request describing what changed and why.

## Principles to keep

- **Never invent the user's facts.** Missing information becomes an open question or a labelled assumption.
- **Original wording.** Do not copy text from standards, certification bodies or published exams.
- **No accounts or branding built in.** Skills must work on a plain Claude account and add no organisation's name to outputs unless the user provides it.
- **Explain the reason** behind an instruction instead of adding rigid rules.
- **Keep it proportionate.** Small projects and small organisations get small answers.

## Arabic terms

Corrections to `arabic-terms.md` are welcome. Please say which source or regional usage your correction follows.

## Licence

By contributing you agree that your contribution is licensed under the MIT licence of this repository.
