# pyttsx3 is an engine which helps to translate text into speech
import pyttsx3
import speech_recognition as sr
import datetime
import os

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
        r.pause_threshold = 2
        try:
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        except Exception:
            speak("I'm sorry, I didn't catch that.")
            return "None"

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
    

if __name__ == '__main__':
    # speak("Hello sir, welcome to the Python AI Assistant! I am Raj. How can I assist you today?")
    # command = takecommand()
    # print(f"Recognized Command: {command}")
    
    wish()
    while True:
        query = takecommand().lower()
        
        #Perform the logic building tasks 
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if 'open youtube' in query:
        #     speak("Opening Youtube...")
        #     webbrowser.open("youtube.com")
        # elif 'open google' in query:
        #     speak("Opening Google...")
        #     webbrowser.open("google.com")
        # elif 'open stackoverflow' in query:
        #     speak("Opening Stack Overflow...")
        #     webbrowser.open("stackoverflow.com")
        # elif 'quit' in query:
        #     speak("Goodbye Sir. Have a great day!")
        #     break
        # elif 'current time' in query:
        #     current_time = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"The current time is {current_time}")
        # elif 'current date' in query:
        #     current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        #     speak(f"The current date is {current_date}")
        # else:
        #     speak("Sorry sir, I didn't understand that. Please try again...") 
        
