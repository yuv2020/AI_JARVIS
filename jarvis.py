# pyttsx3 is an engine which helps to translate text into speech
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Text-to-speech function
def speak(audio):
    """
    Function to convert text to speech.
    :param audio: Text to be spoken
    """
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Speech recognition function
def takecommand():
    """
    Function to take voice input from the user and recognize it.
    :return: Recognized text or "None" if recognition fails
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}")
    except Exception as e:
        speak("Sir, please say it again...")
        return "None"
    return query

#Wish function
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak(f"Good morning! Sir.")
    elif hour > 12 and hour < 16:
        speak(f"Good afternoon! Sir.")
    else:
        speak(f"Good evening! Sir.")
        
    speak("I am jarvis sir! Please tell me How can i assist you todays.")
    
#Send to email
def sendEmail(to, content):
     """
     Function to send an email.
     :param to: Recipient's email  
     :param content: Content of the email
     """
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login("yuvraj252122@gmail.com", "Yuvrajteddy@562003")
     server.sendmail("yuvraj252122@gmail.com", to, content)
     server.close()

if __name__ == '__main__':
      
    wish()
    while True:
    # if 1:
        query = takecommand().lower()
        
        # Perform the logic building tasks 
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            os.system("start cmd")
            
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif 'play music' in query:
            music_dir = "E:\\VIDEOS SONG"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            # for song in songs:
            #     if song.endswith('.mp3'):                    
            #         os.startfile(os.path.join(music_dir, song))
            os.startfile(os.path.join(music_dir, rd))
            
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your current IP address is {ip}")    
            
        elif "wikipedia" in query:
            speak("search wikipedia...")        
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
            
        elif 'open youtube' in query:
            speak("Sir, what should I search on youtube?")
            webbrowser.open("https://www.youtube.com")
            
        elif 'open instagram' in query:
            speak("Sir, what you want to see on instagram?")
            webbrowser.open("https://www.instagram.com")
        
        elif 'open facebook' in query:
            speak("Sir, what should I search for you on facebook?")
            webbrowser.open("https://www.facebook.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open whatsapp' in query:
            webbrowser.open("https://www.whatsapp.com")
        
        elif 'open google' in query:
            speak("Sir, what should I search on google?")
            cm=takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
            speak(f"Searching for {cm} on Google.")
            
        elif 'send message' in query:
            kit.sendwhatmsg("+91 79824 39048", "This is a test message", 2, 00)
            
        elif 'play song on youtube' in query:
            speak("Sir, what song should I play?")
            cm=takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
            speak(f"Playing {cm} on YouTube.")
            # kit.playonyt(cm)
            
        elif 'send an email' in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = 'rajonweb03@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
                
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this email.")
                
        elif 'no' in query:
            speak("Sure, have a great day!")
            sys.exit()
            
        speak("Sir, do yo have any other work.")
                

                
                
            
        
            