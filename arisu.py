import speech_recognition as sr
import os
from gtts import gTTS
from playsound import playsound #pip install playsound==1.2.2

def recognize_phrase(recog, mic):
    audio = recog.listen(mic)
    return recog.recognize_google(audio, language="en-US")
    
def arisu_say(phrase):
   language = 'en'
   output = gTTS(text=phrase, lang=language, slow=False, tld='co.uk')
   output.save("audio.mp3")
   playsound('audio.mp3')
   os.remove("audio.mp3")


recongnition = sr.Recognizer() 
with sr.Microphone() as microphone:
    while True:
        recongnition.adjust_for_ambient_noise(microphone)
        arisu_say("Arisu: Say something...")
        
        try:
            phrase = recognize_phrase(recongnition, microphone)
            print("You: " + phrase)

            if(phrase == "create folder"):
                arisu_say("name the folder")
                answer = recognize_phrase(recongnition, microphone)
                os.mkdir("./" + answer)
                print("success!!!")
                continue
            if(phrase == "open folder"):
                arisu_say("which one?")
                answer = recognize_phrase(recongnition, microphone)
                os.startfile(answer)
                print("done")
                continue
            if(phrase == 'hello'):
                arisu_say("Hello master, what can I do for you?")
                continue
            if(phrase == 'stop'):
                arisu_say("see you soon")
                break
            else:
                arisu_say("I'm sorry, I don't know how to answer that")
        except sr.UnknownValueError:
            arisu_say("Sorry, I didn't understood.")
