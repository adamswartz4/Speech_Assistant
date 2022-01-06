import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def speak(audio_string):
    tts= gTTS(text=audio_string, lang='en')
    r = random.randint(1,10000000)
    audio_file = 'audio-'+ str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
            print('Please try again')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    
    if 'what time is it'  in voice_data:
        speak(ctime())
    if 'what is the date'  in voice_data:
        speak(ctime())
    if 'search' in voice_data:
        search=record_audio('What do you want to search for')
        url= 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is your result for '+ search)
    if 'find location' in voice_data:
        location=record_audio('Where would you like to go?')
        url= 'https://google.nl/maps/place/' + location +'/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of '+ location)

    if 'exit' in voice_data:
        exit()
time.sleep(1)
speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
#print(voice_data)

