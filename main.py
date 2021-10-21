from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import wikipedia
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("good morning boss!")
    elif time>=12 and time<18:
        speak("good afternoon boss!")
    else:
        speak("good evening boss!")
    speak("Boss how can i help uuh!!")

def takeCommand():
    recive_command = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n\t\tListening.......")
        voice = recive_command.listen(source)
    
    try:
        print("\n\t\tRecognizing....")
        command = recive_command.recognize_google(voice)
        command = command.lower()
        if 'sara' in command:
            command = command.replace('sara', '')
            print(f"\t\tBOSS said: {command}\n")

    except Exception as e:
        print("\n\t\tSay that again please...")
        return "None"
    return command

if __name__ == "__main__":
    wishMe()
    while True:
        command = takeCommand().lower()
    
        if 'who is' in command:
            about = command.replace('who is', '')
            information = wikipedia.summary(about, sentences=2)
            speak('According to Wikipedia')
            print(information)
            speak(information)

        elif 'tell me about' in command:
            about = command.replace('tell me about', '')
            information = wikipedia.summary(about, sentences=2)
            speak('According to Wikipedia')
            print(information)
            speak(information)
            
        elif 'play' in command: 
            song = command.replace('play', '')
            speak('playing'+ song)
            pywhatkit.playonyt(song)

        elif 'the time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Currnet time is'+ time)

        elif 'about you' in command:
            print('I am sara, I am made in pthon 3.9.1 and developer mr.Raja Mandal, thanks for asking')
            speak('I am sara, I am made in pthon 3.9.1 and developer mr.Raja Mandal, thanks for asking')
            
        elif 'are you single' in command:
            print('sorry boss, i am in a relationship with wifi')
            speak('sorry boss, i am in a relationship with wifi')

        elif 'thanks' in command:
            print('its my pleasure boss')
            speak('its my pleasure boss')
        elif 'thank you' in command:
            print('its my pleasure boss')
            speak('its my pleasure boss')
    
        elif 'open youtube' in command:
            webbrowser.open('youtube.com')
        elif 'open google' in command:
            webbrowser.open('google.com')
            
        # elif 'sara' and 'play music' in command:
        #     music_dir = 'D:\\videos\\raja\\fev'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
            
        else:
            print("sorry i cannot get, please boss give me command once again")
            speak('sorry i cannot get, please boss give me command once again')
        