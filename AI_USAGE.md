## The log

###  Setup

- Claude created the starter folder for this project: the file structure, empty
  function stubs with comments explaining what each one should do, the CSS
  stylesheet, and the test file. I wrote the actual code inside the functions.


- Claude wrote most of `static/style.css`. I made many iterations based on 
what I needed, for example, I added many new rule sets to customize the stats
 page and the claimed page to make them look visually appealing. I also chose 
 the primary colors for the website.


- Claude wrote `tests/test_matching.py` completely, to give me a target to build
  against. I did not write the tests. I wrote all the code that makes them pass.

- Claude wrote the homepage route in `main.py` and the
  `create_tables` function in `database.py` as examples for me 
  to learn the pattern from.

  AI helped me troubleshoot Python/Pillow compatibility with Python 3.14, understand Git setup errors, 
  and understand how to connect VS Code with GitHub.


### Database

AI explained how SQLite databases work, helped me understand SQL queries, dictionaries, and how to test my database functions. I wrote the database functions and testing code myself.

### Forms

AI explained GET vs. POST requests, helped me understand how HTML form fields connect to Python, and helped me troubleshoot a database error involving a missing photo_filename key. I wrote the form and application code myself.

### Browse and search

AI helped me understand how to build dynamic SQL queries for searching and filtering database items, connect the browse route to the database, and debug my item detail page. I wrote the actual code myself and used AI mainly to review my code and explain errors.

### Matching engine

AI helped me understand and debug the matching engine functions, including cleaning words, finding shared words and colors, checking dates, scoring matches, and finding the best matches. AI explained errors and helped me understand how the matching system should structure its results. I wrote the actual code myself and used AI mainly to review my code, explain errors, and guide me through the tests. I also tested the matching engine with realistic database items and changed the maximum points for shared description words because six meaningful shared words indicated a very strong match, making the original 25-point cap feel too low.

### Match screen and claiming

 AI helped me debug the claim flow, fix the layout of the matched item cards, and understand how to hide claimed items from Browse. I made the changes and tested the app myself.

### Photos and stats

For adding photos and the stat page, I used ChatGPT to help implement and troubleshoot image resizing for uploaded lost and found items. Although the image sizing issue was not completely resolved, I decided the appearance was acceptable and moved on. I made the code changes and tested the results myself.

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
