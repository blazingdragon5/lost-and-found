
import sqlite3

DB_FILE = "items.db"

#This code repeats itself a lot
def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

#This creates the tables where items are stored when sent to the database
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            status            TEXT NOT NULL,
            title             TEXT NOT NULL,
            description       TEXT,
            category          TEXT,
            color             TEXT,
            location          TEXT,
            date_happened     TEXT,
            reporter_name     TEXT,
            reporter_contact  TEXT,
            photo_filename    TEXT,
            created_at        TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            lost_item_id   INTEGER NOT NULL,
            found_item_id  INTEGER NOT NULL,
            score          INTEGER,
            reasons        TEXT,
            confirmed      INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


#------------------------------------------|
#       Basic Database Functions           |
#------------------------------------------|

#This adds an item to the database
def add_item(item):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO items "
    "(status, title, description, category, color, location, "
    "date_happened, reporter_name, reporter_contact, photo_filename) "
    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    (
        item["status"],
        item["title"],
        item["description"],
        item["category"],
        item["color"],
        item["location"],
        item["date_happened"],
        item["reporter_name"],
        item["reporter_contact"],
        item["photo_filename"]
    )
    )
    new_id = cur.lastrowid
    conn.commit()
    conn.close()
    return new_id

#This gets an item from the database based on the id
def get_item(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items WHERE id = ?",
        (item_id,)
    )
    row = cur.fetchone()
    conn.close()
    return row

#This deletes an item from the database based on the id
def delete_item(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM items WHERE id = ?",
        (item_id,)
    )
    conn.commit()
    conn.close()
    return f"Item id: {item_id} deleted from database"

#This gets every item in the database
def get_all_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "Select * FROM items ORDER BY created_at DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

#This gets every item based on if its a lost or found item
def get_items_by_status(status):
    conn=get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items WHERE status = ?",
        (status,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows


#------------------------------------------|
#              Updating Photos             |
#------------------------------------------|


def update_photo_filename(item_id, filename):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET photo_filename = ? WHERE id = ?",
        (filename, item_id)
    )
    conn.commit()
    conn.close()
#This function sets the filename to a specific id

#------------------------------------------|
#       Searching the Database             |
#------------------------------------------|

#This gets every item that satisfies the filters that are currently on
def search_items(query="", status="", category=""):

    conn = get_connection()
    cur = conn.cursor()

    sql = "SELECT * FROM items WHERE 1=1 AND status != 'claimed'"
    params = []

    if query:
       sql += " AND (title LIKE ?)"
       params.append("%" + query + "%")

    if status:
     sql += " AND status = ?"
     params.append(status)

    if category:
       sql += " AND category = ?"
       params.append(category)

    cur.execute(sql, params)
    results = cur.fetchall()
    conn.close()
    return results



#------------------------------------------|
#       Updating Database After match       |
#------------------------------------------|


#This function changes an item's status to claimed
def mark_claimed(item_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE items SET status = ? WHERE id = ?",
        ("claimed",item_id)
    )
    conn.commit()
    conn.close()


#This functions saves a confirmed match to be later used when calculating statistics
def save_match(lost_id, found_id, score, reasons):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
    "INSERT INTO matches (lost_item_id, found_item_id, score, reasons, confirmed) VALUES (?, ?, ?, ?, ?)",
    (lost_id, found_id, score, str(reasons), 1)
)
    conn.commit()
    conn.close()
    


#------------------------------------------|
#       Statistics from Database           |
#------------------------------------------|

def get_stats():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM items")
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM items WHERE status = 'claimed'")
    returned = cur.fetchone()[0]
    waiting = total - returned
    if total == 0:
        return_rate = 0
    else:
        return_rate = returned/total * 100
    return {"reported": total, "returned": returned, "waiting": waiting, "return_rate": return_rate}
#This function counts up all the items in the database, how much are claimed, and how the rate of return for the items.


def get_category_counts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT category, COUNT(*) FROM items GROUP BY category")
    rows = cur.fetchall()
    conn.close()

    return [
        {"name": row[0], "count": row[1]}
        for row in rows
    ]
#This function counts up all the items for every category