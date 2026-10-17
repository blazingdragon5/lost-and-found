
#------------------------------------------|
#                                          |
#       Matching and Scoring Logic         |
#                                          |
#------------------------------------------|

#This list identifies words that should not be used for comparing items.
BORING_WORDS = {
    "a", "an", "the", "my", "i", "it", "is", "was", "in", "on", "at", "to",
    "of", "and", "or", "with", "for", "from", "this", "that", "there", "has",
    "have", "had", "its", "it's", "some", "very", "really", "think", "maybe",
    "lost", "found", "item", "thing", "stuff",
}

#This list identifies colors that can be used to score matches
COLOR_WORDS = {
    "red", "orange", "yellow", "green", "blue", "purple", "pink", "black",
    "white", "gray", "grey", "brown", "silver", "gold", "tan", "navy", "teal",
}


#------------------------------------------|
#       Basic Comparing Functions          |
#------------------------------------------|

def clean_words(text):
    if not text:
        return set()
    text = text.lower()
    for ch in ".,!?:;()/'-":
        text = text.replace(ch, " ")
    words = text.split()
    useful_words = [word for word in words if word not in BORING_WORDS]
    return set(useful_words)


def shared_words(text_a, text_b):
    a = clean_words(text_a)
    b = clean_words(text_b)
    return a & b


def find_colors(text):
    new_text = clean_words(text)
    return new_text & COLOR_WORDS


def dates_make_sense(lost_date, found_date):
    if found_date == None or lost_date == None or found_date == ""  or lost_date == "":
        return True
    if found_date >= lost_date:
        return True
    else:
        return False



#------------------------------------------|
#            Scoring Functions             |
#------------------------------------------|

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