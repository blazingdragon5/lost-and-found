# For Yogesh — how to support this without doing it

*(Adult-facing notes. Aditya doesn't need to read this one.)*

## What's in this folder

A deliberately incomplete project. `main.py`, `database.py`, and `matching.py`
have full docstrings explaining what each function must do, common traps, and
the approach — but the bodies are `pass  # TODO`. Aditya writes them.

Three things are finished on purpose:

- **`static/style.css`** — complete. Design isn't the judged skill, and ten
  weeks of unstyled HTML is a motivation killer. It's logged in `AI_USAGE.md`.
- **`tests/test_matching.py`** — complete. It's a spec: 20 tests that fail now
  and go green as he builds. This gives him an objective "am I done?" signal
  instead of needing you or me to check his work.
- **The home page route** — works, so Week 0 has a verifiable finish line.

## The compliance story

The rules require the student to do the technical development and that AI use
be disclosed. `AI_USAGE.md` is pre-filled with an honest Week 0 entry naming
exactly what was generated. If he keeps it current weekly, the disclosure
writes itself — and a specific, detailed log reads far better to judges than a
vague one.

Worth a conversation with him: the log is an asset, not a confession.

## How to help when he's stuck

The failure mode to avoid is you (or I) fixing it for him. What works better:

1. **"What's the actual error message?"** Reading errors is the skill. Most
   Python errors name the file and line.
2. **"What did you expect to happen, and what happened?"** This alone solves a
   surprising share of bugs.
3. **"Can you print the value right before it breaks?"** `print()` debugging is
   legitimate and it's how he'll find most problems.
4. Only then, come to me — and ideally have him ask, not you.

If he's been stuck more than 30–40 minutes with no movement, that's not
productive struggle anymore, it's just discouraging. Step in then.

## Realistic time budget

4–6 hours a week. The uneven weeks:

- **Week 0** often takes longer than expected. Windows PATH issues, permissions,
  antivirus blocking pip. Budget extra patience, not extra hours.
- **Week 4 (matching)** is the intellectually hardest and most rewarding.
- **Week 7 (user testing)** needs *your* help — getting 5–10 classmates to try
  it may need a teacher's cooperation. Worth arranging in advance; it's the
  highest-value week for the submission.
- **Week 9 (video)** needs a quiet room and a couple of hours. Screen recording
  on Windows: Xbox Game Bar (Win+G) is built in and fine.

## Dates

- **Register** at congressionalappchallenge.us — do this early, not in October
- **Deadline: Monday, October 26, 2026, 12:00 PM EDT** — hard, no extensions
- Video must be public on YouTube or Vimeo, 1–3 minutes

## The one thing that matters most

Finishing something modest beats abandoning something ambitious. If he's behind
in early October, cut features — photos and stats are droppable. The report →
match → claim loop plus a working demo video is a complete, submittable project.
Protect that core.
