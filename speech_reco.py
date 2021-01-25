import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import pyglet
import subprocess

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang= 'en')
    os.remove("C:\\Users\Asus\\Desktop\\PYTHON PROJECTS\\speechRecognition\\audio.mp3")
    tts.save('audio.mp3')

    wmp = r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe"
    media_file = os.path.abspath(os.path.realpath("C:\\Users\Asus\\Desktop\\PYTHON PROJECTS\\speechRecognition\\audio.mp3"))
    p = subprocess.call([wmp, media_file])
def rec_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say.....")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("you said"+' '+data)
    except sr.UnknownValueError:
        print("unkwnV err")
    except sr.RequestError as e:
        print("req err: {0}". format(e))
    return data

def stan(data):
    if "how are you" in data:
        speak('i am fine')
    
time.sleep(2)
speak('what can i do for you ?')
while 1:
    data = rec_audio()
    stan(data)
