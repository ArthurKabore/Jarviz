import speech_recognition
import pyttsx3
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
import winsound

recognizer = speech_recognition.Recognizer()
done = False

# get string and make a audio file to be played
def speak(data):
    tts = gtts.gTTS(data, lang="en-us")
    r = random.randint(1,20000000)
    audio_file = 'audio'+ str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound(audio_file) # play the audio file
    while audio_file:
        try:
            os.remove(audio_file) # remove audio file
        except:
            pass
def ask():
    try:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        return text
    except Exception:
        return "error"

### os manipulation references ###       
#playsound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/ta_da")
#os.system("start C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/ta_da.mp3")
#winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/est_dev.wav", winsound.SND_ASYNC)

#greetings
# winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/welcome.wav", winsound.SND_ASYNC)

#Entering constant voice recognition until i say exit
with speech_recognition.Microphone() as mic:

    while not done:
        text = ask()
        text = text.lower()

        #wake up the butler 
        if text == "butler":
            speak("Your wish is my command")
            text = ask()
            text = text.lower()
            # here are all my commands
            if text == "yo":
                speak("Heyo")

            elif text == "peace":
                done = True 

            elif text == "search":
                speak("What are you looking for")
                search = ask()
                url = 'https://www.google.com/search?q=' + search
                webbrowser.get().open(url)
                speak(f"Here are the results for {search}")

            elif text == "time to work":
                speak("Get it done")
                url = 'https://www.youtube.com/watch?v=oG7jKUHsLfY&list=PLsXJGdN3urCsmRJSMXrFyUCq_7pYOV2Z2&index=1' 
                webbrowser.get().open(url)
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\pycharm')
        
                print("workspace executed")


        elif text == "error":
            print("Still listening :)")
        elif text != "error":
            print("This is what I heard: ",text)

# exit sound
speak("Until next time")
delay = input("Press ENTER to close: ")

