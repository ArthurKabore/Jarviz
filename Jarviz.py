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

### os manipulation references ###       
#playsound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/ta_da")
#os.system("start C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/ta_da.mp3")
#winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/est_dev.wav", winsound.SND_ASYNC)

#greetings
winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/welcome.wav", winsound.SND_ASYNC)

#Entering constant voice recognition until i say exit
with speech_recognition.Microphone() as mic:

    while exit:
        text = ask()

        #wake up the butler 
        if text == "butler":
            winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/hey_king.wav", winsound.SND_ASYNC)
            text = ask()

            # here are all my commands
            if text == "yo":
                winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/wats_gucci.wav", winsound.SND_ASYNC)

            elif text == "peace":
                exit = False 

            elif text == "search":
                winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/wat_info.wav", winsound.SND_ASYNC)
                search = ask()
                url = 'https://www.google.com/search?q=' + search
                webbrowser.get().open(url)
                winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/ta_da.wav", winsound.SND_ASYNC)

            elif text == "time to work":
                winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/est_dev.wav", winsound.SND_ASYNC)
                url = 'https://www.youtube.com/watch?v=oG7jKUHsLfY&list=PLsXJGdN3urCsmRJSMXrFyUCq_7pYOV2Z2&index=1' 
                webbrowser.get().open(url)
                os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\pycharm')
                os.startfile(r'C:/Users/Arthu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Outlook')
                os.startfile(r'C:/Users/Arthu/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Microsoft Teams')
                os.startfile(r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/PremiumSoft/Navicat')
                
                print("workspace executed")


        elif text == "error":
            print("Still listening :)")
        elif text != "error":
            print("This is what I heard: ",text)

# exit sound
winsound.PlaySound("C:/Users/Arthu/Downloads/Etc/Code/Jarviz/sound/peace_and_love.wav", winsound.SND_ASYNC)
delay = input("Press ENTER to close: ")

