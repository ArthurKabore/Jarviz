import speech_recognition
import pyttsx3
import playsound # to play an audio file
import gtts
from playsound import playsound
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os
import subprocess

recognizer = speech_recognition.Recognizer()
exit = True 
# get string and make a audio file to be played
def speak(data):
    tts = gtts.gTTS(data, lang="en-us")
    r = random.randint(1,20000000)
    audio_file = 'audio'+ str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound(audio_file) # play the audio file
    os.remove(audio_file) # remove audio file

def ask():
    try:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        return text
    except Exception:
        return "error"

speak("Welcome back King")

#Entering constant voice recognition until i say exit
with speech_recognition.Microphone() as mic:

    while exit:
        text = ask()
            
        #wake up the butler 
        if text == "butler":
            speak("Hey king")
            text = ask()

            # here are all my commands
            if text == "yo":
                speak("What's gucci")
            if text == "peace":
                exit = False 
                speak("peace and love")
            if text == "search":
                speak("what information do you seek")
                search = ask()
                url = 'https://www.google.com/search?q=' + search
                webbrowser.get().open(url)
                speak("Ta da")
            if text == "time to work":
                speak("you're the best developer in the world")
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\pycharm')
        elif text == "error":
            print("Still listening :)")
        

