import pyttsx3
import datetime
from pywhatkit import sendwhatmsg, sendwhatmsg_instantly
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
import pywhatkit as kit
import sys



engine = pyttsx3.init('sapi5') #MIcrosoft we can take voice
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    elif hour>=16 and hour<22:
        speak("Good Evening")
    else:
        speak("Good Night")
    print("I am Ultron Sir, working on 950 RPM, speed 20 ms. I can perform several tasks for you ,Like surfing websites, Playing music, Searching on Wikipedia, Sending an Email and Telling somes jokes to lighten your mood. Please Let me Know If you want anything now")
    speak("I am Ultron Sir, working on 950 RPM, speed 20 ms. I can perform several tasks for you ,Like surfing websites, Playing music, Searching on Wikipedia, Sending an Email and Telling somes jokes to lighten your mood. Please Let me Know If you want anything now")

def takeCommand():
    #IT takes mic info from User and returns String output

    r = sr.Recognizer() #micInput as r
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: , {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

def sendEmail(to, content):
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adarshtheguru@gmail.com', 'ewvcxlleityivyyh')
    server.sendmail('adarshtheguru@gmail.com',to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 2:
        query = takeCommand().lower()

        #Logic for Executing tasks based on query
        if 'wikipedia' in query:
            speak ('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'open facebook' in query:
            webbrowser.get('chrome').open("facebook.com")

        elif 'open github' in query:
            webbrowser.get('chrome').open("github.com")

        elif 'some joke' in query:
            getJoke= pyjokes.get_joke()
            speak(getJoke)

        elif 'play music' in query:
            music_dir ="E:\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'random music' in query:
            music_dir ="E:\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, The time is {strTime}")

        elif "fine" in query:
            speak("I am great, How about you Sir, Can I help you in something")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adarshji1999@gmail.com"
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")
        
        elif 'send mail on college ID' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adj@sicsr.ac.in"
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")

        elif 'send whatsapp' in query:
            speak("What's the message for whatsapp, Sir")
            cm=takeCommand()
            kit.sendwhatmsg_instantly('+919936350601',cm)

        elif 'play video on youtube' in query:
            speak("What you want to play, Sir")
            cm=takeCommand()
            kit.playonyt(cm)

        elif "no thanks" in query:
            speak("I am very grateful to help you Sir today, Signing off yours Ultron- The Desktop Assistant")
            sys.exit()

        speak("Sir, Do you have any other thing for me?")



