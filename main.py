import speech_recognition as sr
import pyttsx3
import pywhatkit
from LED import *
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'look' in command:
                command = command.replace('look', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'turn on' in command:
        turn_LED()
        talk('turned on')


run_alexa()
