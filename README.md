# ElderSense 🧓🤖

ElderSense is a *voice-assisted health companion* for the elderly. It helps caregivers monitor seniors’ daily medicine intake, hydration, emergencies, and even provides reminders, jokes, and music playback for emotional support.  

---

## 🚀 Features
- ✅ Voice Assistant – Interacts using speech recognition & text-to-speech  
- 💊 Medication Reminders – Reminds at scheduled times & logs medicine intake  
- 📊 SQLite Database – Tracks daily medication status  
- 📧 Emergency Alerts – Sends an email to caregiver when “help” or “emergency” is detected  
- 🎵 Music Player – Plays random songs from the music/ folder  
- 🗣 Friendly Interaction – Jokes, greetings, and wellness check-ins  

---
## 🛠 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ElderSense.git
cd ElderSense
```
### 2. (Optional) Create virtual environment
```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install speechrecognition pyttsx3 pygame
```
### 4. Configure Email Alerts

#### Edit alert_module.py and replace:

SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
CAREGIVER_EMAIL = "caregiver-email@gmail.com"

⚠ Use a Gmail App Password (not your normal password).

### 5. Add Music
#### Place .mp3 or .wav files inside the music/ folder.

### 6. Run the Project
```bash
python app.py
```

---

##📂 Project Structure

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

### 🧪 Example Usage

At 08:30, ElderSense says:

> "⏰ Reminder: Please take your Blood Pressure Tablet. Did you take it?"

If user replies “yes” → medicine logged as ✅ taken.
If user says “help” → caregiver immediately gets an 📧 emergency email.
If user says “play music” → plays a random song.

---

### 📦 Dependencies

speechrecognition
pyttsx3
pygame
smtplib (built-in)
sqlite3 (built-in)


### Install everything with:
```bash
pip install -r requirements.txt
```

##  ▶ Usage

-Example voice commands
- Remind me to take medicine
- Play music
- Call for help

---

## 🏗 Tech Stack

1. Programming Language – Python
2. Framework – Flask (for backend)
3. Libraries – SpeechRecognition, pyttsx3, Pygame
4. Database – SQLite (or your preferred DB)
5. Platform – Cross-platform (Windows/Linux/Mac)
6. Cloud Services (Optional) – AWS / GCP for notifications

---

## 🤝 Contribution

### 1. Fork the repository (on GitHub)
2. Create a new branch
```bash
git checkout -b feature-branch
```
3. Make your changes and commit
```bash
git commit -m "Added new feature"
```
4. Push the branch
```bash
git push origin feature-branch
```
5. Open a Pull Request (on GitHub)
