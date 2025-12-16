import os
import re
import time
import speech_recognition as sr
import itertools
import webbrowser
import pyttsx3
import musiclibrabry

jarvis_counter = itertools.count(1)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def _normalize(text: str) -> str:
    return re.sub(r'[^a-z ]+', '', text.lower())

def ProcessCommand(command):
    c = _normalize(command)
    print(f"Normalized command: {c}")  

    try:
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

        if "open google" in c:
            webbrowser.get(chrome_path).open_new_tab("https://www.google.com")

        elif "open youtube" in c:
            webbrowser.open_new_tab("https://www.youtube.com")

        elif "open facebook" in c:
            webbrowser.open_new_tab("https://www.facebook.com")

        elif "open instagram" in c:
            webbrowser.get(chrome_path).open_new_tab("https://www.instagram.com")

        elif c.lower().startswith("play"):
            song = c.split(" ", 1)[1] if " " in c else ""
            link = musiclibrabry.music[song]
            webbrowser.open(link)
        
        else:
            speak("Please buy the upgraded plan")

    except Exception as e:
        print("Eror", {e})


if __name__ == "__main__":
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening......")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=2, phrase_time_limit=3)

            word = r.recognize_google(audio, language="en-US")
            print(f"Heard: {word!r}")
            norm = _normalize(word)

            if "jarvis" in norm or "hey jarvis" in norm or "hi jarvis" in norm:
                speak("Ya")

                with sr.Microphone() as source:
                    print("Jarvis is active......")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio, language="en-US")
                    print(f"Command: {command}")
                    ProcessCommand(command)

        except Exception as e:
            print("Error:", e)
