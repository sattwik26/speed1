import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'speed' in command:
                command = command.replace('speed', '')
                print(command)
    except:
        pass
    return command


def run_speed():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'what time is it' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is your name' in command:
        talk('speed')
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif 'do you know my name' in command:
        talk('no i dont and please dont tell me. i am low on storage')
    elif 'who created you' in command:
        talk('my creater is sattwik siddamsety')
    elif 'shut down':
        talk('i will shut down when you sleep before 12:30')   
    elif 'who is siddamsety' in command:
        talk('siddamsety is a great business man') 
    elif 'what is a' in command:
        person = command.replace('what is a', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who created' in command:
        person = command.replace('who created', '') 
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    else:
        talk('Please say the command again.')
        
    

while True:
    run_speed()
