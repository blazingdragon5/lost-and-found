"""
main.py — the front door of your app.

Every web page lives here. When someone types an address in their browser,
this file decides what they see.

HOW A ROUTE WORKS
-----------------
    @app.get("/browse")
    def browse_page(request):
        return ...

That @app.get("/browse") line says: "when someone visits /browse, run the
function underneath me." The @ symbol is called a decorator. You don't have
to understand how decorators work internally — just know it's how you glue a
web address to a Python function.

WHAT'S DONE, WHAT'S NOT
-----------------------
The home page works, so you can prove your setup is good (Week 0).
Everything below it is a stub with a TODO. Those are yours.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import database

app = FastAPI(title="School Lost and Found")

# Lets your HTML pages load style.css and any photos.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tells FastAPI your HTML pages live in the templates folder.
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup():
    """Runs one time when the server boots. Makes sure the database exists."""
    database.create_tables()


# ==========================================================================
#  WEEK 0 — this one already works. Start your server and go look at it.
# ==========================================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """The home page."""
    # Later you'll swap these fake numbers for real ones from your database.
    stats = {"reported": 0, "returned": 0, "waiting": 0}
    recent = []

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "stats": stats, "recent": recent},
    )


# ==========================================================================
#  WEEK 2 — reporting items
# ==========================================================================

@app.get("/report/lost", response_class=HTMLResponse)
def report_lost_form(request: Request):
    """Show the 'I lost something' form.

    TODO (Week 2):
      Return templates.TemplateResponse("report.html", {...}).
      Pass "kind": "lost" in the dictionary so the template knows which
      version of the form to draw. One template, two uses — less work for you.
    """
    pass  # TODO: you write this


@app.post("/report/lost")
def submit_lost(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    color: str = Form(...),
    location: str = Form(...),
    date_happened: str = Form(...),
    reporter_name: str = Form(...),
    reporter_contact: str = Form(...),
):
    """Save a lost item, then send the person to their match results.

    Notice this is @app.post, not @app.get. GET means "show me a page."
    POST means "here's some data, save it." Forms use POST.

    TODO (Week 2):
      1. Build a dictionary from all those Form values above.
      2. Add "status": "lost" to it.
      3. new_id = database.add_item(that_dictionary)
      4. return RedirectResponse(f"/item/{new_id}", status_code=303)

    ⚠️ TRAP: you must use status_code=303 on that redirect. Without it the
    browser tries to POST again and you get a confusing error. This one
    wastes people a lot of time.
    """
    pass  # TODO: you write this


@app.get("/report/found", response_class=HTMLResponse)
def report_found_form(request: Request):
    """Show the 'I found something' form.

    TODO (Week 2): same as report_lost_form, but pass "kind": "found".
    """
    pass  # TODO: you write this


@app.post("/report/found")
def submit_found(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    color: str = Form(...),
    location: str = Form(...),
    date_happened: str = Form(...),
    reporter_name: str = Form(...),
    reporter_contact: str = Form(...),
):
    """Save a found item.

    TODO (Week 2): same idea as submit_lost, but "status": "found".
    TODO (Week 6): add photo upload. Come back to this later — don't try
    to do photos and forms at the same time.
    """
    pass  # TODO: you write this


# ==========================================================================
#  WEEK 3 — browsing and searching
# ==========================================================================

@app.get("/browse", response_class=HTMLResponse)
def browse(request: Request, q: str = "", status: str = "", category: str = ""):
    """Show every item, with optional filters.

    Those extra arguments (q, status, category) come from the web address:
        /browse?q=blue&category=Water bottle
    FastAPI pulls them out and hands them to you automatically. Nice, right?

    The = "" part means "if it's not in the address, use an empty string."

    TODO (Week 3):
      items = database.search_items(q, status, category)
      then return templates.TemplateResponse("browse.html", {...})
    """
    pass  # TODO: you write this


# ==========================================================================
#  WEEK 4-5 — the match screen (your best screen)
# ==========================================================================

@app.get("/item/{item_id}", response_class=HTMLResponse)
def item_detail(request: Request, item_id: int):
    """Show one item, plus anything that might match it.

    The {item_id} in the address is a wildcard. Visiting /item/7 means
    item_id gets set to 7.

    TODO (Week 3): get the one item with database.get_item(item_id).
                   Show it. Stop there for now.

    TODO (Week 5): now add the matches.
      1. Figure out which pile to search. If this item is "lost", you want
         to compare it against all the "found" items. And vice versa.
      2. candidates = database.get_items_by_status(the_opposite_status)
      3. matches = matching.find_matches(item, candidates)
      4. Pass matches into the template.
    """
    pass  # TODO: you write this


@app.post("/item/{item_id}/claim")
def claim_item(item_id: int, matched_with: int = Form(...)):
    """Someone pressed "That's mine!" — mark both items as claimed.

    TODO (Week 5):
      Mark BOTH items claimed — the lost one and the found one. It's easy to
      forget the second one, and then a returned item sits in your list
      forever looking like it's still missing.
      Then redirect to a confirmation page.
    """
    pass  # TODO: you write this


# ==========================================================================
#  WEEK 6 — stats
# ==========================================================================

@app.get("/stats", response_class=HTMLResponse)
def stats_page(request: Request):
    """The numbers page. This one goes in your demo video.

    TODO (Week 6):
      Get the counts from database.get_stats() and render stats.html.
      Judges love real numbers, so make this page count.
    """
    pass  # TODO: you write this
