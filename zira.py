import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    
    speak("Hello! I'm Zira, How can i help you!")

def takeInstruction():


    i = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        i.pause_threshold = 0.8
        audio = i.listen(source)

    try:
        print("Recognizing...")
        query = i.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print (e)
        print("I am not able to understand Please try again.")
        return "None"
    return query

if __name__ == "__main__":


    Greetings()
    if 1:
    #while True:
       query = takeInstruction().lower()

       if 'wikipedia' in query:
           speak("Searching Wikipedia...")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
           webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

       elif 'open gmail' in query:
           webbrowser.open("gmail.com")

       elif 'play music' in query:
           music_dir = "C:\\Users\\DELL\\OneDrive\\Desktop\\music"
           songs = os.listdir(music_dir)
           x = random.randint(0, len(songs)+1)
           song_no = int(x)
           os.startfile(os.path.join(music_dir,songs[song_no]))

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(strTime)
           speak(f"The time is {strTime}\n")

       elif 'open pycharm' in query:
           path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
           os.startfile(path)
