import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Optional: Configure voice properties
engine.setProperty("rate", 150)      # Speed of speech (default ~200)
engine.setProperty("volume", 1.0)    # Volume (0.0 to 1.0)

# If multiple voices available (male/female), pick one
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)   # 0 = male, 1 = female (depends on system)


def speak(text):
   def speak(text):
       import pyttsx3

def speak(text):
    engine = pyttsx3.init(driverName='sapi5')   # force Windows driver
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)   # try first voice
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    

def listen():
    """Listen from microphone and return recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)  
            text = r.recognize_google(audio)
            print(f"✅ You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            print("⏳ Timeout: no speech detected")
            return ""
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError:
            print("⚠ API unavailable or internet issue")
            return ""