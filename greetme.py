
import datetime

import pyttsx3


# Text to speech
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)

def speak(audio): #hear audio is var which contaim text
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty("rate",170)

def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("good morning sir i am virtual assistent jarvis")
    elif hour >12 and hour<=18:
        speak("good afternoon sir i am virtual assistent jarvis")
    else:
        speak("good eVENING sir i am virtual assistent jarvis")
    speak("Please tell me, how can i help you ?")
