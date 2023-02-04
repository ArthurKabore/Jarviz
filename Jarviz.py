from datetime import datetime
from logging.config import listen
import speech_recognition as sr
import pyttsx3 
import webbrowser
import os
import openai

# Initiating ChatGPT API
openai.api_key = "" # Use your own key. This can get expensive :) 

# Test reqest
openai.Edit.create(
  model="text-davinci-edit-001",
  input="What day is it?",
  instruction="Fix the spelling mistakes"
)

# Speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 0 = male, 1 = female
 
# Configure browser
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
 
def speak(text, rate = 180):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
 
def parseCommand():
    listener = sr.Recognizer()
    print('Listening...')
    
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        input_speech = listener.listen(source)
 
    try: 
        print('Recognizing...')
        query = listener.recognize_google(input_speech, language='en_us')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'

    return query.lower()

if __name__ == '__main__':
    speak('Booting up')
 
    while True:
        speak('Waiting for orders')
        input = parseCommand()

        # Activate command section
        if input == "help":
            speak('How can I help')
            input = parseCommand()

            # Navigation & searching
            if input == 'search':
                speak('What do you wish to find')
                input = parseCommand()
                url = 'https://www.google.com/search?q=' + input
                webbrowser.get().open(url)
 
            # Note taking
            if input == 'note':
                speak('Ready to record your note')
                newNote = parseCommand().title()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note written')

            # Open workspace
            if input == "work":
                os.startfile(r'C:\Users\Arthur\AppData\Local\Programs\Microsoft VS Code')
                webbrowser.get().open("https://www.youtube.com/watch?v=588vxxSSMh0") 

        # Exit
        if input == 'exit':
            speak('Goodbye')
            break

