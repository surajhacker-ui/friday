import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyautogui
import time
import requests


engine = pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voices into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 2
        audio = r.listen(source,timeout=2,phrase_time_limit=2)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning,sir")
    elif hour>12 and hour<18:
        speak("good afternoon,sir")
    else:
        speak("good evening,sir")
    speak("I AM FRIDAY please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('surajrockzz9@gmail.com','SH3rD4vj8KcfhnE')
    server.sendmail('surajrockzz9@gmail.com',to,content)
    server.close()

#for news updates
def news():
   main_url = "http://newsapi.org/v2/top-headlines?sources=tehcrunch&apikey=358a9a36e2ef416d8675fb555a53b1b4"

   main_page = requests.get(main_url).json()
   #print(main_page)
   articles = main_page["articles"]
   #print("articles")
   head = []
   day = ["first,second,third,fourth,fifth,sixth,seventh,eighth,ninth,tenth"]
   for ar in articles:
       head.append(ar["title"])
   for i in range(len(day)):
       #print(f"today's {day[1]} news is:", head[1])
       speak(f"today's {day[1]} news is:",{head[1]})


if __name__ == '__main__':
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\SysWOW64\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
            os.startfile(apath)

        elif "open cmd" in query:
            os.system("start cmd")

        elif "play music" in query:
            music_dir = "E:\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stack overflow.com")

        elif "open google" in query:
            speak("sir, what should i search for you")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919495823041", "this is testing protoccol",0,0)

        elif "play songs on youtube" in query:
            kit.playonyt("dynamite")

        elif "email to suraj" in query:
            try:
                speak("what should i say")
                content = takecommand().lower()
                to = "sresmi872@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to suraj")

            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send email")


        elif "no thanks" in query:
            speak("thanks for using me sir,have a nice day")
            sys.exit()

# to close any application
        elif "close notepad" in query:
            speak("okay sir,closing notepad")
            os.system('taskkill /f /in notepad.exe')

# to set alarm
        elif "alarm" in query:
            nn = int(datetime.datetime.now().hour())
            if nn == 22:
                music_dir = "E:\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

#shutdown the system
        elif"shutdown the system" in query:
            os.system("shutdown /s /t S")

        elif"restart the system" in query:
            os.system("shutdown /r /t s")

        elif"sleep the system" in query:
            os.system("rundll32.exe powerprof.d11,setsuspendstate 0,1,0")


        elif "friday switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif"tell me news" in query:
            speak("please wait sir,fetching the news")
            news()

            speak("sir,do you have any other work")

    





