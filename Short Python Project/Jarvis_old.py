from http import server
from re import search
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
#import smtplib
import random
import requests
import sys
from requests import get
from bs4 import BeautifulSoup
#import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


'''def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('arnab112datta@gmail.com','anita2003datta')
    server.sendmail('arnab112datta',to,content)
    server.close()'''


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("Sir I am jarvis. Please tell me how  I can help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("do you have any other work sir...")   
        print("do you have any other work sir...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube...')

        elif 'thanks' in query or 'thank you' in query:
            speak("its my pleasure,sir")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak('opening facebook...')

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak('opening instagram...')

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak('opening whatsapp...')

        elif 'open makaut' in query:
            webbrowser.open("https://makaut1.ucanapply.com/smartexam/public/")
            speak('opening makaut...')

        elif 'open telegram' in query:
            webbrowser.open("https://web.telegram.org/k/")
            speak('opening telegram...')

        elif 'open github' in query:
            webbrowser.open("https://github.com/arnabdatta03")
            speak('opening github...')
        
        elif 'open mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm#inbox")
            speak('opening mail...')
        
        elif 'open link tree' in query:
            webbrowser.open("https://linktr.ee/arnabdatta03")
            speak('opening link tree...')
            
        elif 'who make you' in query:
            speak('arnab sir,make me and he is my boss')
            print('Arnab sir,make me and he is my boss')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google...')

        elif 'play music' in query:
            music_dir = "C:\\Users\\arnabdatta\\Desktop\\Music"
            songs = os.listdir(music_dir)
            speak('playing music...')
            rd = random.choice(songs)
            print(songs)    
            os.startfile(os.path.join(music_dir, rd))   
        
        elif 'stop' in query:
            speak(" ok sir,you can call me anytime,have a good day.")
            sys.exit()

        elif "weather" in query:
         search = "weather in durgapur"
         url = f"https://www.google.com/search?q={search}"
         r = requests.get(url)
         data = BeautifulSoup(r.text,"html.parser")
         weather = data.find("div",class_="BNeawe").text
         speak(f"current{search} is {weather}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif "open notepad" in query:
            npath = "C:\\Users\\arnabdatta\\Documents\\jarvis.txt"
            os.startfile(npath)
            speak('opening notepad...')

        elif "open document" in query:
            npath = "C:\\Users\\arnabdatta\\Documents"
            os.startfile(npath)
            speak('opening document...')

        elif "open cmd" in query:
            npath = "C:\\Users\\arnabdatta\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            os.startfile(npath)
            speak('opening command...')

        elif "open photo" in query:
            npath = "C:\\Users\\arnabdatta\\Pictures"
            os.startfile(npath)
            speak('opening photos...')

        elif "open download" in query:
            npath = "C:\\Users\\arnabdatta\\Downloads"
            os.startfile(npath)
            speak('opening Laptop download files...')
        
        elif "open chrome" in query:
            npath = "C:\\Users\\Public\\Desktop\\Google Chrome.lnk" 
            os.startfile(npath)
            speak('opening chrome...')
        
        elif "vs code" in query:
            npath = "C:\\Users\\arnabdatta\\Desktop\\Visual Studio Code.lnk"
            os.startfile(npath)
            speak('opening vs code...')

        elif "open dev " in query:
            npath = "C:\\Users\\arnabdatta\\Desktop\\Dev-C++.lnk"
            os.startfile(npath)
            speak('opening dev c and c++...')

        elif "open music" in query:
            npath = "C:\\Users\\arnabdatta\\Music"
            os.startfile(npath)
            speak('opening music from file...')

        elif "ip address" in query:
            ip= get('https://api.ipify.org').text
            print(ip)
            speak(f"sir your IP address is{ip}")

        #else:
            search = 'https://www.google.com/search?q='+query #bujhta na parle direct google a search kora daba
            webbrowser.open(search)



        