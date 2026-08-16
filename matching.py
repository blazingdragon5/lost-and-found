"""
matching.py — ⭐ THE BRAIN OF YOUR APP ⭐

This is the file that makes your project different from every other
"I built a website with forms" submission. Spend your best hours here.

THE JOB
-------
Somebody lost a blue Hydro Flask. You have 30 found items sitting in a bin.
Which ones might be theirs, and how sure are you?

Your answer is a number from 0 to 100, plus a list of reasons in plain English.
The reasons matter as much as the number — judges remember "it told me WHY."

HOW YOU'LL BUILD IT
-------------------
Five small steps, each worth points. Add them up, cap at 100.

    Step 1  Same category?      hard filter — no match if not
    Step 2  Do the dates work?  hard filter — can't be found before it's lost
    Step 3  Shared words        up to 40 points   <- the interesting one
    Step 4  Same color          25 points
    Step 5  Same place          20 points
            Same category       15 points (you already checked it, now score it)

Those point values are my suggestion, not the law. Try them, look at the
results, then change them. Making a 92% feel like a real 92% is called tuning,
and it's a legit engineering job. Mention it in your video.

⚠️ BUILD THESE IN ORDER, ONE AT A TIME.
Write clean_words() first. Run `pytest` and get its test passing. THEN write
the next one. If you write all six functions and then run the tests, you'll
have six broken things at once and no idea which is which. One at a time is
slower for ten minutes and faster for two weeks.

Run your tests like this:

    pytest                     (run everything)
    pytest -k clean_words      (run just the one you're working on)
"""

# Words too common to be useful. "blue" tells you something. "the" doesn't.
# Add more as you notice them — this list is yours to grow.
BORING_WORDS = {
    "a", "an", "the", "my", "i", "it", "is", "was", "in", "on", "at", "to",
    "of", "and", "or", "with", "for", "from", "this", "that", "there", "has",
    "have", "had", "its", "it's", "some", "very", "really", "think", "maybe",
    "lost", "found", "item", "thing", "stuff",
}

COLOR_WORDS = {
    "red", "orange", "yellow", "green", "blue", "purple", "pink", "black",
    "white", "gray", "grey", "brown", "silver", "gold", "tan", "navy", "teal",
}


# ==========================================================================
#  STEP 1 — clean_words()   ← START HERE. This is your first function.
# ==========================================================================

def clean_words(text):
    """Turn a sentence into a set of useful, comparable words.

    Example:
        clean_words("Dark BLUE bottle, covered in stickers!")
        -> {"dark", "blue", "bottle", "covered", "stickers"}

    Notice what happened:
      - everything got lowercased  ("BLUE" and "blue" must count as the same)
      - punctuation got dropped    ("stickers!" and "stickers" must match)
      - boring words got tossed    ("in" is gone)
      - it's a SET, not a list     (no duplicates, and sets can do overlap math)

    HOW TO WRITE IT:
      1. text = text.lower()
      2. Replace punctuation with spaces. Easiest way:
             for ch in ".,!?;:()\"'-/":
                 text = text.replace(ch, " ")
      3. words = text.split()
      4. Keep only words that are NOT in BORING_WORDS
      5. return set(words)

    ⚠️ TRAP: if text is None (an item with no description), .lower() crashes
    the whole page. Handle it — `if not text: return set()` on the first line.

    TODO: you write this.
    """
    pass  # TODO: you write this


# ==========================================================================
#  STEP 2 — shared_words()
# ==========================================================================

def shared_words(text_a, text_b):
    """Find the words that appear in BOTH descriptions.

    Example:
        a = "blue Hydro Flask with stickers"
        b = "blue metal water bottle covered in stickers"
        shared_words(a, b)  ->  {"blue", "stickers"}

    This is the actual core idea of your matching engine, and it's the thing
    to explain in your demo video. Real search engines do a fancier version
    of exactly this.

    HOW TO WRITE IT:
      Clean both texts into sets, then use the & operator.
      set_a & set_b gives you everything in both. Python does the work.

    TODO: you write this.
    """
    pass  # TODO: you write this


# ==========================================================================
#  STEP 3 — find_colors()
# ==========================================================================

def find_colors(text):
    """Pull any color words out of a description.

    Example:
        find_colors("dark blue bottle with a red cap")  ->  {"blue", "red"}

    Color is a strong signal. People forget the brand but they remember
    "it was blue."

    HOW TO WRITE IT:
      You already have clean_words(). Use it, then keep only the words that
      are also in COLOR_WORDS. That's the & operator again.

    Reusing a function you already wrote instead of starting over is a real
    skill — notice you're doing it here.

    TODO: you write this.
    """
    pass  # TODO: you write this


# ==========================================================================
#  STEP 4 — dates_make_sense()
# ==========================================================================

def dates_make_sense(lost_date, found_date):
    """True if the found date is on or after the lost date.

    You can't find a jacket on Monday that gets lost on Friday. This one
    rule alone throws out a surprising amount of junk.

    Your dates come in as text like "2026-10-02". Lucky break: that format
    sorts correctly as plain text, because it goes big-unit to small-unit.
    "2026-10-03" > "2026-10-02" just works. So you can compare the strings
    directly — no date library needed.

    (This is why the YYYY-MM-DD format is used everywhere in programming.
    Now you know why.)

    ⚠️ If either date is missing, return True. Better to show a maybe-match
    than to silently hide a real one.

    TODO: you write this.
    """
    pass  # TODO: you write this


# ==========================================================================
#  STEP 5 — score_match()   ← the big one. Do this after the four above work.
# ==========================================================================

def score_match(item_a, item_b):
    """Compare two items. Return a score 0-100 and a list of reasons.

    Give back a dictionary shaped like this:

        {
            "score": 92,
            "reasons": [
                {"good": True,  "text": "Same category - water bottle"},
                {"good": True,  "text": "2 words in both: blue, stickers"},
                {"good": False, "text": "Different place"},
            ]
        }

    Your template loops over "reasons" to draw the ✓ and ✗ lines you saw in
    the mockup. That's why each reason carries a good True/False.

    HOW TO WRITE IT — go in this order:

      1. score = 0, reasons = []

      2. HARD FILTER: if categories differ, return {"score": 0, "reasons": []}
         right away. Don't waste time scoring a backpack against a water bottle.

      3. HARD FILTER: figure out which item is the lost one and which is the
         found one, then call dates_make_sense(). If it fails, score 0, stop.

      4. Same category  -> score += 15, add a good reason

      5. words = shared_words(a's description, b's description)
         Each shared word is worth 10 points, up to 40 max:
             word_points = min(len(words) * 10, 40)
         Add a reason listing the actual words — that's the line that makes
         people go "whoa, it really read my description."

      6. Colors: if find_colors() overlaps -> score += 25

      7. Same location -> score += 20

      8. return {"score": min(score, 100), "reasons": reasons}

    ⚠️ Cap the score with min(score, 100). Otherwise a really good match shows
    "115% match" and it looks broken even though your math was fine.

    TODO: you write this. Take your time — this is the heart of it.
    """
    pass  # TODO: you write this


# ==========================================================================
#  STEP 6 — find_matches()
# ==========================================================================

def find_matches(item, candidates, minimum_score=25, limit=5):
    """Score one item against a whole pile, best matches first.

    This is what main.py actually calls. It's short — it just runs
    score_match() over and over and sorts the results.

    HOW TO WRITE IT:
      1. results = []
      2. Loop through candidates. For each one:
           - skip it if it's the same item (check the ids!)
           - result = score_match(item, candidate)
           - if result["score"] >= minimum_score, keep it (store the candidate
             AND the score AND the reasons together)
      3. Sort highest score first:
             results.sort(key=lambda r: r["score"], reverse=True)
         reverse=True is what makes it descending. Leave it off and you show
         your WORST match first, which is a funny bug to demo.
      4. return results[:limit]      <- just the top few

    Why minimum_score=25: below that it's noise, and a wall of 8% matches
    makes your app look dumb. Cutting off junk is a design decision, and
    it's worth saying out loud in your video that you made it on purpose.

    TODO: you write this.
    """
    pass  # TODO: you write this
