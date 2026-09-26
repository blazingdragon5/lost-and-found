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
    if not text:
        return set()
    text = text.lower()
    for ch in ".,!?:;()/'-":
        text = text.replace(ch, " ")
    words = text.split()
    useful_words = [word for word in words if word not in BORING_WORDS]
    return set(useful_words)


# ==========================================================================
#  STEP 2 — shared_words()
# ==========================================================================

def shared_words(text_a, text_b):
    a = clean_words(text_a)
    b = clean_words(text_b)
    return a & b


# ==========================================================================
#  STEP 3 — find_colors()
# ==========================================================================

def find_colors(text):
    new_text = clean_words(text)
    return new_text & COLOR_WORDS


# ==========================================================================
#  STEP 4 — dates_make_sense()
# ==========================================================================

def dates_make_sense(lost_date, found_date):
    if found_date == None or lost_date == None or found_date == ""  or lost_date == "":
        return True
    if found_date >= lost_date:
        return True
    else:
        return False



# ==========================================================================
#  STEP 5 — score_match()   ← the big one. Do this after the four above work.
# ==========================================================================

def score_match(item_a, item_b):
    score = 0 
    reasons = []

    #Hard filter about category
    if item_a["category"] != item_b["category"]:
        score = 0 
        return {"score":0, "reasons": []}
    else: 
        score += 15
        reasons.append({"good": True, "text": "Same type of item"})

    #Hard filter about dates
    if dates_make_sense(item_a["date_happened"],item_b["date_happened"]) == False:
        score = 0
        return {"score":0, "reasons": []}
    
    #Point counter for matching words
    words = shared_words(item_a["description"], item_b["description"])
    if len(words)>0:
        score += min(len(words)*10, 50)
        reasons.append({"good" : True, "text" : f"{len(words)} words matching in description : {', '.join(words)}"})
    else:
        reasons.append({"good":False, "text": "No words matching in description"})

    #Point counter for common colors
    colors = find_colors(item_a["color"]) & find_colors(item_b["color"])
    if len(colors)>0:
        score += min(len(colors)*15, 30)
        reasons.append({"good" : True, "text" : f"{len(colors)} common colors: {', '.join(colors)}"})
    else:
        reasons.append({"good": False, "text" : "No common colors between items"})

    #Assigns Points for location
    if item_a["location"] == item_b["location"]:
        score += 20
        reasons.append({"good": True, "text": f"Both items found or lost in {item_a['location']}"})
    else:
        reasons.append({"good": False, "text": "Found and lost in different locations"})

    return {"score": min(score,100), "reasons": reasons}
    


# ==========================================================================
#  STEP 6 — find_matches()
# ==========================================================================

def find_matches(item, candidates, minimum_score=25, limit=5):
    results = []
    for candidate in candidates:
        if candidate["id"] == item["id"]:
            continue
        if item["status"] == "lost":
            result = score_match(item, candidate)
        else:
            result = score_match(candidate, item)
        if result["score"]>=minimum_score:
            result["item"] = candidate
            results.append(result)
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:limit]