from database import init_db, log_medication, get_medication_logs
from voice_module import listen, speak
from alert_module import send_emergency_email
from reminder_module import start_reminders
from music_module import play_music,stop_music
import time
from database import get_daily_status


def main():
    init_db()

    speak("Hello Grandma! Did you sleep well? Don’t forget to drink water.")
    start_reminders()

    # Example: AI reminds at 08:30
    now = time.strftime("%H:%M")
    if now == "08:30":
        speak("⏰ Reminder: Please take your Blood Pressure Tablet. Did you take it?")
        response = listen().lower()

        if "yes" in response:
            log_medication("Blood Pressure Tablet", "08:30", True)
            speak("✅ Great! I stored that you took your medicine.")
        else:
            log_medication("Blood Pressure Tablet", "08:30", False)
            speak("❌ Okay, I stored that you have not taken it yet.")



# Show today's medicine status
    status = get_daily_status()
    print("Today’s Medicine Status:")
    print("Morning Tablet:", status["morning"])
    print("Afternoon Tablet:", status["afternoon"])
    print("Night Tablet:", status["night"])

    while True:
        user_input = listen()

        if not user_input:
            speak("Hmm, I didn’t catch that. Can you repeat?")
            continue
        
        if any(word in user_input for word in ["medicine", "tablet", "pill", "took", "taken"]):
            log_medication("Blood Pressure Medicine", "08:30", True)
            speak("Great job! I’ve logged that you took your medicine.")

        elif any(word in user_input for word in ["bye", "goodbye"]):
            speak("Goodbye Grandma. Take care.")
            break
       
        elif "emergency" in user_input or "fallen" in user_input or "help" in user_input:
            speak("⚠ Emergency detected. Sending email to caregiver.")
            send_emergency_email("ElderSense")
            speak("✅ Emergency email has been sent successfully.")
        elif "water" in user_input or "drink" in user_input:
            speak("Good! Staying hydrated is very important. I’ll log this for you.")
        elif "not well" in user_input or "sick" in user_input or "pain" in user_input:
            speak("I’m sorry you’re not feeling well. I’ll notify your caregiver.")
            send_emergency_email("Grandma is not feeling well")
        elif "joke" in user_input:
            speak("Why don’t scientists trust atoms? Because they make up everything! Haha.")
        elif "song" in user_input:
            speak("🎵 La la la… I’m singing a happy tune for you, Grandma!")
        elif "good morning" in user_input:
            speak("Good morning Grandma! I hope you have a wonderful day.")
        elif "good night" in user_input:
            speak("Good night Grandma, sweet dreams.")
        elif "good afternoon" in user_input:
            speak("Good afternoon Grandma.")
        elif "good evening" in user_input:
            speak("Good evening Grandma.")
        elif "play music" in user_input:
            speak("Playing one of your favorite songs, Grandma!")
            play_music()
        elif "stop music" in user_input:
            speak("okay grandma , stopping the music")
            stop_music()
        
        else:
            speak("Hmm, I didn’t quite get that. Can you repeat?")


if __name__ == "__main__":
    main()