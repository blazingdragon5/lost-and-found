# School Lost & Found

A web app that helps students get their lost stuff back. When you report
something you lost, it searches everything that's been turned in and shows you
the closest matches — and explains why it thinks they match.

Built for the 2026 Congressional App Challenge.

**Aditya — this file is your submission's front door.** Judges and anyone
visiting your GitHub read it first. Right now it's a skeleton with TODOs. Fill
it in during Week 8, once you know what you actually built.

---

## The problem

TODO (Week 8): Write 3-4 sentences about your school's lost and found. Use
what you learned from talking to the front office and your friends. Real
numbers if you have them — "our school throws out about X items every June"
hits much harder than "lost and found is disorganized."

## What it does

- Report a lost item
- Report a found item, with a photo
- Search and filter everything
- **Suggests matches with a 0–100 confidence score and plain-English reasons**
- Mark items as claimed
- Stats page showing return rate

## How the matching works

TODO (Week 8): Explain your scoring in your own words. Walk through one real
example — the blue water bottle is a good one. Show the score and the reasons.

This section is the most important part of the README. It's where you prove
there's real thinking behind the app instead of just forms and a database.

## Built with

Python · FastAPI · SQLite · Jinja2 · Pillow

See `CREDITS.md` for the full list of libraries and `AI_USAGE.md` for how AI
was used.

## Running it yourself

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000

## Testing

```bash
pytest
```

## What I learned

TODO (Week 8): The hardest bug you fixed and how you figured it out. What you'd
do differently. This is a question on the submission form too, so writing it
here means it's already done.

## What's next

TODO (Week 8): Image matching, notifications, school accounts, an iPhone app.
Having a real roadmap shows you're thinking past the deadline.

---

Built by Aditya S. · 2026 Congressional App Challenge
