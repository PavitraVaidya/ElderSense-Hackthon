# reminder_module.py
import time
import threading
import sqlite3
from voice_module import speak, listen
from database import log_medication, mark_taken

# ✅ Define Grandma's daily schedule
SCHEDULE = {
    "08:30": "Morning Tablet",
    "13:00": "Afternoon Tablet",
    "21:00": "Night Tablet"
}


def reminder_loop():
    while True:
        now = time.strftime("%H:%M")

        # Check if current time matches one of the schedule times
        if now in SCHEDULE:
            med_name = SCHEDULE[now]
            message = f"⏰ Reminder: Please take your {med_name}. Did you take it?"
            print(message)
            speak(message)

            # listen for Grandma’s answer
            response = listen().lower()
            if "yes" in response:
                confirm = f"Great! Marking {med_name} as taken ✅"
                print(confirm)
                speak(confirm)
                log_medication(med_name, now, True)
            else:
                not_taken = f"Okay, I’ll note that you haven’t taken {med_name} yet ❌"
                print(not_taken)
                speak(not_taken)
                log_medication(med_name, now, False)

            # wait 60 seconds so it doesn’t repeat within the same minute
            time.sleep(60)

        time.sleep(10)  # check every 10 seconds


def start_reminders():
    """Start the reminder loop in a separate thread."""
    t = threading.Thread(target=reminder_loop, daemon=True)
    t.start()