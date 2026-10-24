## The log

###  Setup

- AI created the starter folder for this project: the file structure with each file labeling what each file should do,
 most of the CSS stylesheet, and the test file. I wrote the actual code inside each file


- AI wrote most of `static/style.css`. I made many iterations based on 
what I needed, for example, I added many new rule sets to customize the stats
 page and the claimed page to make them look visually appealing. I also chose 
 the primary colors for the website.


- AI wrote `tests/test_matching.py` completely, to give me a target to build
  against. I did not write the tests. I wrote all the code that makes them pass.

- AI wrote the homepage route in `main.py` and the
  `create_tables` function in `database.py` as examples for me 
  to learn the pattern from.


- AI helped me troubleshoot Python/Pillow compatibility with Python 3.14, understand Git setup errors, 
  and understand how to connect VS Code with GitHub.


### Database

AI explained how SQLite databases work, helped me understand SQL queries, dictionaries, and how to test my database functions. I wrote the database functions and testing code myself.

### Forms

AI explained GET vs. POST requests, helped me understand how HTML form fields connect to Python, and helped me troubleshoot a database error involving a missing photo_filename key. I wrote the form and application code myself.

### Browse and search

AI helped me understand how to build dynamic SQL queries for searching and filtering database items, connect the browse route to the database, and debug my item detail page. I wrote the actual code myself and used AI mainly to review my code and explain errors.

### Matching engine

AI helped me understand and debug the matching engine functions, including cleaning words, finding shared words and colors, checking dates, scoring matches, and finding the best matches. AI explained errors and helped me understand how the matching system should structure its results. I wrote the actual code myself and used AI mainly to review my code, explain errors, and guide me through the tests. I also tested the matching engine with realistic database items and changed the maximum points for shared description words because six meaningful shared words indicated a very strong match, making the original 25-point cap feel too low.



## Summary

Although I used AI as a learning and troubleshooting resource throughout the development of my Lost & Found App, I completed most of the project independently. I wrote the majority of the application's code myself, made the main decisions about its functionality and design, and worked through errors by testing, debugging, and revising my own implementation. AI served primarily as a guide to help me understand unfamiliar concepts, resolve difficult problems, and improve my code rather than building the entire application for me. I took responsibility for connecting the different parts of the app, checking that features worked correctly, and making adjustments based on my own testing. Overall, AI supported my learning and development process, but the majority of the programming, problem-solving, and decision-making was my own work.
