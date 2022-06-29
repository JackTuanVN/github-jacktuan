from urllib.parse import quote_from_bytes
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
EDITH = pyttsx3.init()
voice = EDITH.getProperty('voices')
EDITH.setProperty('voice',voice[1].id)
def speak(audio):
    print('E.D.I.T.H.: ' + audio)
    EDITH.say(audio)
    EDITH.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Tuan")
    elif hour >=12 and hour <18:
        speak("Good Afternoon Tuan")
    elif hour >=18 and hour <24:
        speak("Good Night Tuan")
    speak('How can I help you')
def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Tuan : " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input("Your order is: "))
    return query
if __name__ =="__main__":
    welcome() 
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search boss? ")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("What should I search boss? ")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video" in query:
            video = r"D:\đám cưới\New folder\VTS_01_1.mp4"
            os.startfile(video)
        elif "time" in query:
            time()
        elif "goodbye" in query:
            speak("EDITH is quiting sir. Goodbye Tuan")
            quit()