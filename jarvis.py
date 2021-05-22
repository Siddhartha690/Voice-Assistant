import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    #this fn takes a string and speaks it
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello sir I am Jarvis How may i help you")


def takecommand():
    #it takes microphone input from user and return string output

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
        #print(e)
        print("Say that again Please...")
        return "None"
    return query


# this function is to send email to someone
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", 'your-password')
    server.sendEmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takecommand().lower()
    
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching  Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackovwerflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open animepahe' in query:
            webbrowser.open("animepahe.com")

        elif 'play music' in query:
            music_dir = 'path_of_your_music_folder'
            songs = os.listdir(music_dir)
            for i in songs:
                os.startfile(os.path.join(music_dir, i))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open visual studio code' in query:
            code_path = "path_of_your_vs_code"
            os.startfile(code_path)

        elif 'email to receiver_name' in query:
            try:
                speak("What should i say?")
                content = takecommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email")

        elif 'quit' in query:
            exit()

