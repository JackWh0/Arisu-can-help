import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound #pip install playsound==1.2.2
from datetime import datetime

now = datetime.now()
current_hour = int(now.strftime("%H"))

recongnition = sr.Recognizer() 
name = "master"

def recognize_phrase(recog, mic):
    print("listening...")
    recongnition.adjust_for_ambient_noise(microphone)
    audio = recog.listen(mic)
    text = recog.recognize_google(audio, language="en-US")
    text = text.lower()
    return text
    
def arisu_say(phrase):
   language = 'en'
   output = gTTS(text=phrase, lang=language, slow=False, tld='co.uk')
   output.save("audio.mp3")
   playsound('audio.mp3')
   os.remove("audio.mp3")

def greeting():
    if(current_hour >= 0 and current_hour <= 4):
        return "Wow you're still awake "
    if(current_hour > 4 and current_hour <= 11):
        return "Good morning "
    if(current_hour > 11 and current_hour < 18):
        return "Good afternoon "

    return "Good evening"

with sr.Microphone() as microphone:
    arisu_say(greeting() + "{fname}".format(fname=name))
    
    while True:
        arisu_say("I'm waiting for commands...")
        
        try:
            phrase = recognize_phrase(recongnition, microphone)
            print("You: " + phrase)

            if(phrase in "create folder"):
                arisu_say("name the folder")
                answer = recognize_phrase(recongnition, microphone)
                os.mkdir("./" + answer)
                print("success!!!")
                continue
            if(phrase in "open folder"):
                arisu_say("which one?")
                answer = recognize_phrase(recongnition, microphone)
                os.startfile(answer)
                print("done")
                continue
            if(phrase in "delete folder"):
                #ToDo
                continue
            if(phrase in 'hello'):
                arisu_say("Hello {fname}".format(fname=name))
                continue
            if(phrase in 'who are you'):
                arisu_say("What do you mean? Did you forget me? I'm Arisu, your personal helper.")
                continue
            if(phrase in 'call me something else'):
                arisu_say("Okay {fname}, how would you like me to call you?".format(fname=name));
                name = recognize_phrase(recongnition, microphone)
                print("You: " + phrase)
                arisu_say("Alright, now I gonna call you {fname}".format(fname=name))
                continue
            if(phrase in 'stop'):
                arisu_say("Ok {fname}, see you soon!".format(fname=name))
                break
            else:
                arisu_say("I'm sorry, I don't know how to answer that")
        except sr.RequestError:
            # API was unreachable or unresponsive
            print("API unavailable")
        except sr.UnknownValueError:
            print("You: " + phrase)
            arisu_say("Sorry, I didn't understood.")
