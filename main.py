from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import matching
import database

app = FastAPI(title="School Lost and Found")

# Lets your HTML pages load style.css and any photos.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tells FastAPI your HTML pages live in the templates folder.
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup():
    database.create_tables()


# ==========================================================================
#  WEEK 0 — this one already works. Start your server and go look at it.
# ==========================================================================

@app.get("/", response_class=HTMLResponse)
def home123(request: Request):
    stats = {"reported": 0, "returned": 0, "waiting": 0}
    recent = database.get_all_items()[:4]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "stats": stats, "recent": recent},
    )


# ==========================================================================
#  WEEK 2 — reporting items
# ==========================================================================

@app.get("/report/lost", response_class=HTMLResponse)
#This code displays the form for the user
def report_lost_form(request: Request):
    return templates.TemplateResponse(
    "report.html",
    {"request": request, "kind": "lost"},
)
#This code opens the report_lost_item form 
    


@app.post("/report/lost")
#This posts the data from the form app 
def submit_lost(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    color: str = Form(...),
    location: str = Form(...),
    date_happened: str = Form(...),
    reporter_name: str = Form(...),
    reporter_contact: str = Form(...),
    #This takes the data from the form and saves it in these variables
):
    item = {
    "status": "lost",
    "title": title,
    "description": description,
    "category": category,
    "color": color,
    "location": location,
    "date_happened": date_happened,
    "reporter_name": reporter_name,
    "reporter_contact": reporter_contact,
    "photo_filename": None,
    }
    new_id = database.add_item(item)
    return RedirectResponse(f"/item/{new_id}", status_code=303)
#This function takes the data from the form and saves it in a new dictionary called item.
#Then it sends the item to the database and gets back the id.


@app.get("/report/found", response_class=HTMLResponse)
#This code displays the form for the user
def report_found_form(request: Request):
    return templates.TemplateResponse(
        "report.html",
        {"request":request, "kind": "found"}
    )
#This code opens the report_found_form


@app.post("/report/found")
#This posts the data from the form
def submit_found(
    title: str = Form(...),
    description: str = Form(...),
    category: str = Form(...),
    color: str = Form(...),
    location: str = Form(...),
    date_happened: str = Form(...),
    reporter_name: str = Form(...),
    reporter_contact: str = Form(...),
    #This saves the data from the submit_found form in variables
):
     item = {
        "status": "found",
        "title": title,
        "description": description,
        "category": category,
        "color": color,
        "location": location,
        "date_happened": date_happened,
        "reporter_name": reporter_name,
        "reporter_contact": reporter_contact,
        "photo_filename": None,
        }
     new_id = database.add_item(item)
     return RedirectResponse(f"/item/{new_id}", status_code=303)
   
   # TODO (Week 6): add photo upload. Come back to this later — don't try
    #to do photos and forms at the same time.
#This function takes the data from the found form and enters it into the database.


# ==========================================================================
#  WEEK 3 — browsing and searching
# ==========================================================================

@app.get("/browse", response_class=HTMLResponse)
def browse(request: Request, q: str = "", status: str = "", category: str = ""):

    results = database.search_items(q,status,category)
    return templates.TemplateResponse(
    "browse.html",
    {"request": request, "results": results, "q" : q , "status": status, "category": category},
    )
#This function uses the data from the filter bar in browse.html to send data to
#search_items in database.py which fins the items in those filters and returns it to this function
#Then, it uses that data to make item cards which will be displayed

# ==========================================================================
#  WEEK 4-5 — the match screen (your best screen)
# ==========================================================================

@app.get("/item/{item_id}", response_class=HTMLResponse)
def item_detail(request: Request, item_id: int):
#
    item = database.get_item(item_id)

    if item is None:
     return HTMLResponse("Item not found", status_code=404)
    x = item["status"]
    if x == "claimed":
       results = None
    else: 
       pile = "found" if item["status"] == "lost" else "lost"
       candidates = database.get_items_by_status(pile)
       results = matching.find_matches(item, candidates)
    return templates.TemplateResponse(
        "item_detail.html",
        {"request": request, "item":item, "results" : results}
    )
#This function gives a personal screen to every item when you click on it
#You can click from the homepage, the browse page, or it opens when you fill out a form
#It also passes a results variables with matches that will show on the item_detail html page


@app.post("/item/{item_id}/claim")
def claim_item(request: Request, item_id: int, matched_with: int = Form(...)):
    database.mark_claimed(item_id)
    database.mark_claimed(matched_with)
    item1 = database.get_item(item_id)
    item2 = database.get_item(matched_with)
    if item1["status"] == "lost":
        itemv1 = item1
        itemv2 = item2
    else: 
        itemv1 = item2
        itemv2 = item1
    match = matching.score_match(item1,item2)
    pickup_code = "LF-" + str(item2["id"]).zfill(4)
    database.save_match(item_id, matched_with,match["score"], match["reasons"])
    return templates.TemplateResponse(
        "claimed.html",
        {"request": request, "item1": itemv1, "item2":itemv2, "code": pickup_code, "reporter": item2}
    )
#This function first changes the status of both items to claimed
#Then it calculates the score and sends it to save_match function along with the ids
#Then it shows the claimed.html page

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
