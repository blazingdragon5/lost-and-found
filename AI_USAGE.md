# AI Usage Log

**Aditya: fill this in every single week. Two minutes, and it saves you from
scrambling in October.**

The Congressional App Challenge rules say AI can help with parts of a project
but can't build the whole thing, and that any AI use has to be disclosed. When
you submit, you'll be asked about this. If you've kept this log, you paste it
in and you're done. If you haven't, you'll be trying to remember what happened
in September while a deadline clock is running.

Be specific and be honest. "Claude explained how X works, I wrote the code" is
a great answer. Judges have read a lot of submissions — a real, detailed log
reads as confidence. A vague one reads as hiding something.

---

## What counts as worth logging

- Something explained to you (a concept, an error message, how a library works)
- Help finding a bug
- Structure or starter files you were given
- Code you were shown — **especially** this one. Say what it was and whether
  you typed it yourself or used it as-is.

## What doesn't need logging

- Looking things up in the official Python or FastAPI docs
- Googling an error and reading Stack Overflow
- Asking a human for help (but that's worth mentioning in your write-up anyway)

---

## The log

### Week 0 — Aug 15–23 — Setup

- Claude created the starter folder for this project: the file structure, empty
  function stubs with comments explaining what each one should do, the CSS
  stylesheet, and the test file. I wrote the actual code inside the functions.
- Claude wrote `static/style.css` completely. I did not write the CSS. I chose
  the colors and changed [TODO: write what you changed].
- Claude wrote `tests/test_matching.py` completely, to give me a target to build
  against. I did not write the tests. I wrote all the code that makes them pass.
- Claude wrote the working parts of `main.py` (the home page route) and
  `database.py` (`create_tables`) as examples for me to learn the pattern from.

  AI helped me troubleshoot Python/Pillow compatibility with Python 3.14, understand Git setup errors, and understand how to connect VS Code with GitHub.
  AI explained the setup steps and Git commands when I got stuck; I completed the setup and wrote the project code myself.

### Week 1 — Aug 24–30 — Database

Week 1: AI explained how SQLite databases work, helped me understand SQL queries, dictionaries, and how to test my database functions. I wrote the database functions and testing code myself.

### Week 2 — Aug 31–Sep 6 — Forms

Week 2: AI explained GET vs. POST requests, helped me understand how HTML form fields connect to Python, and helped me troubleshoot a database error involving a missing photo_filename key. I wrote the form and application code myself.

### Week 3 — Sep 7–13 — Browse and search

Week 3: AI helped me understand how to build dynamic SQL queries for searching and filtering database items, connect the browse route to the database, and debug my item detail page. I wrote the actual code myself and used AI mainly to review my code and explain errors.

### Week 4 — Sep 14–20 — Matching engine

AI helped me understand and debug the matching engine functions, including cleaning words, finding shared words and colors, checking dates, scoring matches, and finding the best matches. AI explained errors and helped me understand how the matching system should structure its results. I wrote the actual code myself and used AI mainly to review my code, explain errors, and guide me through the tests. I also tested the matching engine with realistic database items and changed the maximum points for shared description words because six meaningful shared words indicated a very strong match, making the original 40-point cap feel too low.

### Week 5 — Sep 21–27 — Match screen and claiming

 AI helped me debug the claim flow, fix the layout of the matched item cards, and understand how to hide claimed items from Browse. I made the changes and tested the app myself.

### Week 6 — Sep 28–Oct 4 — Photos and stats

- TODO

### Week 7 — Oct 5–11 — User testing

- TODO

### Week 8 — Oct 12–18 — Polish and tests

- TODO

### Week 9 — Oct 19–25 — Video and submission

- TODO

---

## Summary for the submission form

Write this in Week 9, after reading back through everything above.

Something like: *"I used Claude as a tutor, not a code generator. It gave me
the project skeleton — empty functions with comments describing what each one
needed to do — plus the CSS and the test file. I wrote all of the application
logic myself, including the matching engine, which is the core of the project.
When I got stuck, I asked for explanations of the concept rather than the
answer. Full week-by-week log below."*

Then paste the log. Don't polish it into something it wasn't — the specifics
are what make it believable.
