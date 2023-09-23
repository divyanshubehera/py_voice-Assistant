import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pygoogle
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone()  as source:
            print('listening...')
            voice = listener.listen(source)
            command=listener.recognize_google(voice)
            command = command.lower()
            if 'ayush' in command:
                # engine.say('hello i am ayush')
                # engine.say('what can i do for you ?')
                # engine.runAndWait()
                command = command.replace('ayush','')
                print(command)
    except:
        pass
    return command

def run_bot():
    command =take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.now.strftime('%I:%M %p')
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,2)
        talk(info)
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    elif 'google' in command:
        data = command.replace('google','')
        info_google = pygoogle(data)
        talk(info_google)
run_bot()