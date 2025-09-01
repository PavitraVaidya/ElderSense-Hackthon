import sqlite3

DB_NAME = "eldersense.db"

def init_db():
    """Initialize the database and create the medication table if it does not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS medication (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medication TEXT NOT NULL,
        time TEXT NOT NULL,
        taken INTEGER NOT NULL DEFAULT 0,      -- 0 = not taken, 1 = taken
        reminded INTEGER NOT NULL DEFAULT 0,   -- 0 = not reminded, 1 = reminded
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

def get_daily_status():
    """
    Returns the status of Grandma's morning, afternoon, and night tablets.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT medication, time, taken
        FROM medication
        WHERE date(timestamp) = date('now')
        ORDER BY time
    """)
    rows = cursor.fetchall()
    conn.close()

    status = {"morning": None, "afternoon": None, "night": None}

    for med, t, taken in rows:
        if "08:" in t or "09:" in t:   # Morning (8–9 AM)
            status["morning"] = "✅ Taken" if taken == 1 else "❌ Not taken"
        elif "14:" in t or "15:" in t: # Afternoon (2–3 PM)
            status["afternoon"] = "✅ Taken" if taken == 1 else "❌ Not taken"
        elif "20:" in t or "21:" in t: # Night (8–9 PM)
            status["night"] = "✅ Taken" if taken == 1 else "❌ Not taken"

    return status

def log_medication(medication, time_str, taken):
    """
    Log a medication entry into the database.
    taken = 1 if user confirmed taking medicine, 0 otherwise.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO medication (medication, time, taken, reminded) VALUES (?, ?, ?, ?)",
        (medication, time_str, int(taken), 0)   # reminded = 0 initially
    )
    conn.commit()
    conn.close()


def mark_taken(reminder_id):
    """Marks a reminder as taken in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE medication SET taken = 1 WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()


def mark_reminded(reminder_id):
    """Marks a reminder as delivered in the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE medication SET reminded = 1 WHERE id = ?", (reminder_id,))
    conn.commit()
    conn.close()


def get_pending_reminders():
    """Fetch all medications that have not yet been reminded."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, medication, time FROM medication WHERE reminded = 0")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_medication_logs():
    """Fetch all medication logs sorted by time."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medication ORDER BY time")
    rows = cursor.fetchall()
    conn.close()
    return rows