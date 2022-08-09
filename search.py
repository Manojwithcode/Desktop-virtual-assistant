from ast import Try
import queue
from unittest import result
import  speech_recognition as sr
import pyttsx3
import pywhatkit as kt
import wikipedia
import webbrowser





engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",170)
print(voices)

def speak(audio): #hear audio is var which contaim text
    engine.say(audio)
    engine.runAndWait()


def takecomm():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source,0,4)

    try:
        print("Recognining....")
        query = r.recognize_google(audio,language='en-in')
        print(f":You said :{query}\n")
    except Exception:
       # speak("error...")
        print("Network connection error")
        return "none"
    return query

def searchgoogle(query):
   
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")

        try:
            kt.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
 
        except:
            speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        kt.playonyt(query)
        speak("Done, Sir")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        speak("According to wikipedia..")
        print(results)
        speak(results)

