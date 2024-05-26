import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour <= 12:
        print("Good Morning..")
        speak("Good Morning..")
    elif hour >= 13 and hour <= 15:
        print("Good afternoon...")
        speak("Good afternoon...")
    elif hour >= 16 and hour <= 18:
        print("Good evening...")
        speak("Good evening...")
    else:
        print("Try to complete your work soon and go to bed...")
        speak("Try to complete your work soon and go to bed...")


