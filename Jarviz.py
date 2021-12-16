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
from io import BytesIO

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

speak("Welcome back King")

while exit:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            if text == "hello":
                speak("Hey man")
            if text == "quit":
                exit = False 
                speak("Buh bye")
            print(f"Recognized: {text}")
    except Exception as e:
        if e:
            speak("Couldn't hear that")
        recognizer = speech_recognition.Recognizer()
        continue
    
