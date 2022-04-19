import speech_recognition as sr
import os

recongnition = sr.Recognizer() 
with sr.Microphone() as microphone:
    while True:
        recongnition.adjust_for_ambient_noise(microphone)
        print("Arisu: Say something...")
        audio = recongnition.listen(microphone)
        try:
            phrase = recongnition.recognize_google(audio, language="en-US")
            print("You: " + phrase)

            if(phrase == "create folder"):
                print("Arisu: name the folder")
                audio = recongnition.listen(microphone)
                answer = recongnition.recognize_google(audio, language="en-US")
                os.mkdir("./" + answer)
                print("success!!!")
                continue
            if(phrase == "open folder"):
                print("Arisu: which one?")
                audio = recongnition.listen(microphone)
                answer = recongnition.recognize_google(audio, language="en-US")
                os.startfile(answer)
                print("done")
                continue
            if(phrase == 'hello'):
                print("Arisu: Hello master, what can I do for you?")
                continue
            if(phrase == 'stop'):
                print("Arisu: see you soon")
                break
        except sr.UnknownValueError:
            print("Arisu:  sorry, I didn't understood.")
