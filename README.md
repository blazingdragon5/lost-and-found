# School Lost & Found

A web app that helps students get their lost stuff back. When you report
something you lost, it searches everything that's been turned in and shows you
the closest matches — and explains why it thinks they match. It then proceeds 
to show the contact information from the reporter along with a pickup code so 
you can get your item back quickly and safely.

Built for the 2026 Congressional App Challenge.
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

One of the hardest bugs I 

## What's next

Of course, my app isn't finished yet I still have many more things to do, 
this is my future roadmap about what features I can add next:

- 
-
-

---

Built by Aditya Sawant · 2026 Congressional App Challenge
