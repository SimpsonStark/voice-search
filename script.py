
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()

r = sr.Recognizer()

mic = sr.Microphone()

engine.say("Welcome to this platform. Please Say the things you need, and say Exit to close. Please say the things you want with their quantity separated by dash")
engine.runAndWait()

while True:
    with mic as source:
        audio = r.listen(source)
    
    try:
        output = r.recognize_google(audio)
        print(output)
        
        if output == 'exit':
            engine.say("Closing Application, Thanks for using")
            engine.runAndWait()
            break
        engine.say("Successfully Entered, Please say the Next thing or say Exit to Close")
        engine.runAndWait()
    except:
        engine.say("Sorry I didn't understand, please say again")
        engine.runAndWait()

    
    

