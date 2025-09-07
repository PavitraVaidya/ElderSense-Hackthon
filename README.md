ElderSense 🧓🤖

ElderSense is a voice-assisted health companion for the elderly.
It helps caregivers monitor seniors’ daily medicine intake, hydration, emergencies, and even provides reminders, jokes, and music playback for emotional support.


---

🚀 Features

✅ Voice Assistant – Interacts using speech recognition & text-to-speech.

💊 Medication Reminders – Reminds at scheduled times & logs medicine intake.

📊 SQLite Database – Tracks daily medication status.

📧 Emergency Alerts – Sends an email to caregiver when “help” or “emergency” is detected.

🎵 Music Player – Plays random songs from the music/ folder.

🗣 Friendly Interaction – Jokes, greetings, and wellness check-ins.



---

🛠 Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/ElderSense.git
cd ElderSense

2. Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

3. Install dependencies

pip install -r requirements.txt

4. Configure Email Alerts

Edit alert_module.py and replace:

SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
CAREGIVER_EMAIL = "caregiver-email@gmail.com"

⚠ Use a Gmail App Password (not your normal password).

5. Add Music

Place .mp3 or .wav files inside the music/ folder.

6. Run the Project

python app.py


---

📂 Project Structure

ElderSense/
│── app.py                # Main application
│── alert_module.py        # Emergency email alerts
│── database.py            # SQLite DB for medicine tracking
│── reminder_module.py     # Scheduled reminders
│── music_module.py        # Music playback
│── voice_module.py        # Speech recognition + TTS
│── eldersense.db          # SQLite database (auto-created)
│── music/                 # Folder containing songs
│── requirements.txt       # Dependencies


---

🧪 Example Usage

At 08:30, ElderSense says:

> "⏰ Reminder: Please take your Blood Pressure Tablet. Did you take it?"



If user replies “yes” → medicine logged as ✅ taken.

If user says “help” → caregiver immediately gets an 📧 emergency email.

If user says “play music” → plays a random song.



---

📦 Dependencies

speechrecognition

pyttsx3

pygame

smtplib (built-in)

sqlite3 (built-in)


Install everything with:

pip install -r requirements.txt
