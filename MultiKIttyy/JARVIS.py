import speech_recognition as sr
from speech_recognition import *
import pyttsx3
import webbrowser
import datetime
import wikipedia


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not understand that.")
        return None
    return query

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you today?")
    while True:
        query = listen()
        if query:
            query = query.lower()
            if "stop" in query:
                speak("Goodbye!")
                break
            elif "search for" in query:
                search_query = query.replace("search for", "")
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.get().open(url)
                speak(f"Here are the results for {search_query}")
            elif "what time is it" in query:
                now = datetime.datetime.now().strftime("%H:%M")
                speak(f"The time is {now}")
            elif "tell me about" in query:
                topic = query.replace("tell me about", "")
                summary = wikipedia.summary(topic, sentences=2)
                speak(summary)
            else:
                speak(f"You said: {query}")
