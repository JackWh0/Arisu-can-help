import speech_recognition as sr
import os

def recognize_phrase(recog, mic):
    audio = recog.listen(mic)
    return recog.recognize_google(audio, language="en-US")
    

recongnition = sr.Recognizer() 
with sr.Microphone() as microphone:
    while True:
        recongnition.adjust_for_ambient_noise(microphone)
        print("Arisu: Say something...")
        
        try:
            phrase = recognize_phrase(recongnition, microphone)
            print("You: " + phrase)

            if(phrase == "create folder"):
                print("Arisu: name the folder")
                answer = recognize_phrase(recongnition, microphone)
                os.mkdir("./" + answer)
                print("success!!!")
                continue
            if(phrase == "open folder"):
                print("Arisu: which one?")
                answer = recognize_phrase(recongnition, microphone)
                os.startfile(answer)
                print("done")
                continue
            if(phrase == 'hello'):
                print("Arisu: Hello master, what can I do for you?")
                continue
            if(phrase == 'stop'):
                print("Arisu: see you soon")
                break
            else:
                print("I'm sorry, I don't know how to answer that")
        except sr.UnknownValueError:
            print("Arisu:  sorry, I didn't understood.")
