"""
database.py — where your app remembers things.

Right now, if you restart your server, everything is gone. A database fixes
that. SQLite is a database that's just... a single file on your computer
(items.db). No installing anything, no server. It's perfect for this.

THE ONE THING TO UNDERSTAND
---------------------------
Every time you talk to the database, it's the same four steps:

    conn = get_connection()          # 1. open the file
    cur = conn.cursor()              # 2. get something to type commands with
    cur.execute("SQL GOES HERE")     # 3. run a command
    conn.commit()                    # 4. save (only needed when CHANGING data)
    conn.close()                     #    always close when you're done

SQL is a second little language just for databases. You only need four words
of it: SELECT (read), INSERT (add), UPDATE (change), DELETE (remove).

⚠️ THE BIGGEST TRAP IN THIS WHOLE FILE
--------------------------------------
When you put values into SQL, use ? placeholders. ALWAYS.

    GOOD:  cur.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    BAD:   cur.execute("SELECT * FROM items WHERE id = " + str(item_id))

The bad version lets someone type sneaky text into your form and wreck your
whole database. It's called SQL injection, it's one of the most common security
holes on the internet, and the ? fixes it completely. Free security — take it.

⚠️ SECOND TRAP: a one-item tuple needs a comma. (item_id,) not (item_id).
Python needs that comma to know it's a tuple. Forget it and you get a
baffling error message.
"""

import sqlite3

DB_FILE = "items.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


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


# ==========================================================================
#  WEEK 1 — your first real code. Start here.
# ==========================================================================

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

def get_all_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "Select * FROM items ORDER BY created_at DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def get_items_by_status(status):
    """Get all items that are "lost", or all that are "found".

    You'll lean on this hard in Week 5: to match a lost item, you grab
    every found item and compare against them.

    TODO (Week 1):
      SELECT * FROM items WHERE status = ?
    """
    pass  # TODO: you write this
    conn=get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM items WHERE status = ?",
        (status,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows


# ==========================================================================
#  WEEK 3 — searching
# ==========================================================================

def search_items(query="", status="", category=""):
    """Find items matching whatever filters were filled in.

    The tricky part: any of these three might be empty, and empty means
    "don't filter on this." So you have to build the SQL up piece by piece.

    Here's the pattern that makes it easy — copy this shape:

        sql = "SELECT * FROM items WHERE 1=1"
        params = []

        if query:
            sql += " AND (title LIKE ? OR description LIKE ?)"
            params.append("%" + query + "%")
            params.append("%" + query + "%")

        if status:
            sql += " AND status = ?"
            params.append(status)

        ... same idea for category ...

        cur.execute(sql, params)

    Why "WHERE 1=1"? It's always true, so it changes nothing — but it means
    every filter you bolt on can start with " AND " without you needing to
    check whether it's the first one. Small trick, saves a lot of if-statements.

    The % signs around the query are SQL's wildcards. "%blue%" means "has the
    word blue anywhere in it."

    TODO (Week 3): write it.
    """
    pass  # TODO: you write this


# ==========================================================================
#  WEEK 5 — closing the loop
# ==========================================================================

def mark_claimed(item_id):
    """Change one item's status to "claimed".

    TODO (Week 5):
      UPDATE items SET status = ? WHERE id = ?
      Don't forget conn.commit() — UPDATE changes data, so it needs saving.
    """
    pass  # TODO: you write this


def save_match(lost_id, found_id, score, reasons):
    """Record that two items were matched up.

    You don't strictly need this for the app to work — but it means you can
    show "23 items returned" on your stats page, and that number is one of
    the best things you'll have in your demo video. Worth it.

    TODO (Week 5): INSERT into the matches table.
    """
    pass  # TODO: you write this


# ==========================================================================
#  WEEK 6 — stats
# ==========================================================================

def get_stats():
    """Count things up for the stats page.

    Return a dictionary like:
        {"reported": 47, "returned": 23, "waiting": 6, "return_rate": 49}

    TODO (Week 6):
      SELECT COUNT(*) FROM items                          -> total
      SELECT COUNT(*) FROM items WHERE status = 'claimed' -> returned
      COUNT(*) gives back a row, so read it with row[0].

    ⚠️ Watch out for dividing by zero when you compute the percentage. On day
    one you have 0 items, and 23/0 crashes your whole page. Check for zero first.
    """
    pass  # TODO: you write this
