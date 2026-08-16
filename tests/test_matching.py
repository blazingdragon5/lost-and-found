"""
test_matching.py — your answer key.

These tests describe exactly what your matching code has to do. I wrote them
for you on purpose: they turn a vague goal ("make matching work") into a
checklist that tells you the second you're right.

RUN THEM:
    pytest                    -> everything
    pytest -k clean_words     -> just the clean_words ones
    pytest -v                 -> show every test by name

RIGHT NOW EVERY ONE OF THESE FAILS. That is correct and expected. Your job
over Weeks 4-5 is to turn them green one at a time.

Work top to bottom. The tests are in the same order as the functions in
matching.py, and each one builds on the last.

A word on what you're doing here: writing code against tests that already
exist is called test-driven development, and a lot of professional software
gets built exactly this way. You're not doing a school exercise version of
it — this is the real thing.
"""

import sys
import os

# Lets this file find matching.py in the folder above it.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matching


# =====================================================================
#  clean_words()  — get these passing first
# =====================================================================

def test_clean_words_lowercases():
    """"BLUE" and "blue" have to count as the same word."""
    assert matching.clean_words("BLUE Bottle") == {"blue", "bottle"}


def test_clean_words_removes_punctuation():
    """"stickers!" should match "stickers"."""
    assert matching.clean_words("bottle, stickers!") == {"bottle", "stickers"}


def test_clean_words_drops_boring_words():
    """"in" and "the" tell you nothing about the item."""
    result = matching.clean_words("the bottle in the bag")
    assert "the" not in result
    assert "in" not in result
    assert result == {"bottle", "bag"}


def test_clean_words_handles_empty():
    """An item with no description must not crash your app."""
    assert matching.clean_words("") == set()
    assert matching.clean_words(None) == set()


# =====================================================================
#  shared_words()
# =====================================================================

def test_shared_words_finds_overlap():
    """The example straight out of your plan."""
    a = "blue Hydro Flask with a bunch of stickers"
    b = "blue metal water bottle covered in stickers"
    assert matching.shared_words(a, b) == {"blue", "stickers"}


def test_shared_words_none_in_common():
    """Two totally different things share nothing."""
    assert matching.shared_words("red backpack", "green notebook") == set()


# =====================================================================
#  find_colors()
# =====================================================================

def test_find_colors_finds_them():
    assert matching.find_colors("dark blue bottle with a red cap") == {"blue", "red"}


def test_find_colors_ignores_non_colors():
    """"bottle" is not a color."""
    assert matching.find_colors("metal bottle") == set()


# =====================================================================
#  dates_make_sense()
# =====================================================================

def test_found_after_lost_is_fine():
    assert matching.dates_make_sense("2026-10-02", "2026-10-03") is True


def test_found_same_day_is_fine():
    """Lost it and found it the same day — totally normal."""
    assert matching.dates_make_sense("2026-10-02", "2026-10-02") is True


def test_found_before_lost_is_impossible():
    """You can't find something that isn't lost yet."""
    assert matching.dates_make_sense("2026-10-05", "2026-10-01") is False


def test_missing_dates_are_allowed():
    """Don't hide a real match just because someone skipped the date field."""
    assert matching.dates_make_sense(None, "2026-10-03") is True
    assert matching.dates_make_sense("2026-10-03", "") is True


# =====================================================================
#  score_match()
# =====================================================================

# Two items that really should match — the water bottle from your mockup.
LOST_BOTTLE = {
    "id": 1, "status": "lost",
    "title": "Blue Hydro Flask",
    "description": "Dark blue metal bottle covered in stickers",
    "category": "Water bottle", "color": "Blue",
    "location": "Gym", "date_happened": "2026-10-02",
}

FOUND_BOTTLE = {
    "id": 2, "status": "found",
    "title": "Blue metal water bottle",
    "description": "Blue metal bottle with stickers all over it",
    "category": "Water bottle", "color": "Blue",
    "location": "Gym", "date_happened": "2026-10-03",
}

FOUND_BACKPACK = {
    "id": 3, "status": "found",
    "title": "Black backpack",
    "description": "Black Jansport backpack",
    "category": "Backpack / bag", "color": "Black",
    "location": "Bus", "date_happened": "2026-10-03",
}


def test_great_match_scores_high():
    """Same category, same color, same place, shared words -> should be strong."""
    result = matching.score_match(LOST_BOTTLE, FOUND_BOTTLE)
    assert result["score"] >= 80


def test_different_category_scores_zero():
    """A backpack is never someone's water bottle. Hard filter."""
    result = matching.score_match(LOST_BOTTLE, FOUND_BACKPACK)
    assert result["score"] == 0


def test_score_never_goes_above_100():
    """A '115% match' looks broken. Cap it."""
    result = matching.score_match(LOST_BOTTLE, FOUND_BOTTLE)
    assert result["score"] <= 100


def test_match_explains_itself():
    """The reasons are the whole point. Don't return a bare number."""
    result = matching.score_match(LOST_BOTTLE, FOUND_BOTTLE)
    assert len(result["reasons"]) > 0
    for reason in result["reasons"]:
        assert "good" in reason
        assert "text" in reason


def test_impossible_dates_score_zero():
    """Found three days before it was lost — not a match, no matter how similar."""
    time_traveler = dict(FOUND_BOTTLE)
    time_traveler["date_happened"] = "2026-09-29"
    result = matching.score_match(LOST_BOTTLE, time_traveler)
    assert result["score"] == 0


# =====================================================================
#  find_matches()
# =====================================================================

def test_best_match_comes_first():
    """Sorted highest score first. Get reverse=True right."""
    weak = dict(FOUND_BOTTLE)
    weak["id"] = 4
    weak["description"] = "plain bottle"
    weak["color"] = "Silver"
    weak["location"] = "Library"

    results = matching.find_matches(LOST_BOTTLE, [weak, FOUND_BOTTLE])
    assert results[0]["score"] >= results[-1]["score"]


def test_junk_is_filtered_out():
    """The backpack shouldn't show up at all."""
    results = matching.find_matches(LOST_BOTTLE, [FOUND_BACKPACK])
    assert len(results) == 0


def test_item_never_matches_itself():
    """Check the ids, or your app will proudly report a 100% match with itself."""
    results = matching.find_matches(LOST_BOTTLE, [LOST_BOTTLE])
    assert len(results) == 0


def test_only_top_few_come_back():
    """Ten decent matches is overwhelming. Show the best 5."""
    many = []
    for i in range(10):
        c = dict(FOUND_BOTTLE)
        c["id"] = 100 + i
        many.append(c)
    results = matching.find_matches(LOST_BOTTLE, many, limit=5)
    assert len(results) <= 5
