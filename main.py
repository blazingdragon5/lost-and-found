from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import matching
import database
from PIL import Image


app = FastAPI(title="School Lost and Found")

# Lets your HTML pages load style.css and any photos.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tells FastAPI your HTML pages live in the templates folder.
templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup():
    database.create_tables()


#------------------------------------------|
#               Homepage                   |
#------------------------------------------|

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    results = database.get_stats()
    stats = {"reported": results["reported"], "returned": results["returned"], "waiting": results["waiting"]}
    recent = database.get_all_items()[:4]
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "stats": stats, "recent": recent},
    )


#------------------------------------------|
#       Reporting and Saving Items         |
#------------------------------------------|

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
    photo: UploadFile = File(None)
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
    #This code processes the photo
    if photo and photo.filename:
        extension = photo.filename.rsplit(".", 1)[-1].lower()

        if extension not in ["jpg", "jpeg", "png"]:
            return {"error": "Please upload a JPG or PNG image."}

        filename = f"item_{new_id}.jpg"

        img = Image.open(photo.file)
        img.thumbnail((800,800))
        img.save("static/uploads/" + filename)

        database.update_photo_filename(new_id, filename)

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


#This posts the data from the form app 
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
    photo: UploadFile = File(None)
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

    #This code processes the photo
    if photo and photo.filename:
        extension = photo.filename.rsplit(".", 1)[-1].lower()

        if extension not in ["jpg", "jpeg", "png"]:
            return {"error": "Please upload a JPG or PNG image."}

        filename = f"item_{new_id}.jpg"

        img = Image.open(photo.file)
        img.thumbnail((800,800))
        img.save("static/uploads/" + filename)

        database.update_photo_filename(new_id, filename)

    return RedirectResponse(f"/item/{new_id}", status_code=303)
   
   # TODO (Week 6): add photo upload. Come back to this later — don't try
    #to do photos and forms at the same time.
#This function takes the data from the found form and enters it into the database.


#------------------------------------------|
#              Finding Items               |
#------------------------------------------|

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

#------------------------------------------|
#       Matching and Item Screens          |
#------------------------------------------|

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

#------------------------------------------|
#           Statistics of the App          |
#------------------------------------------|

@app.get("/stats", response_class=HTMLResponse)
def stats_page(request: Request):
    stats = database.get_stats()

    categories = database.get_category_counts()
    biggest_count = max(
        (category["count"] for category in categories),
        default=0
    )
    biggest_count += 0.5 

    return templates.TemplateResponse(
        "stats.html",
        {"request": request,
          "stats": stats,
          "categories": categories,
          "biggest_count":biggest_count
          })
#This function first calls the get_stats function and saves the dictionary of values in a variable "stats"
#Then it sends the dictionary from this variable to stats.html and shows that page