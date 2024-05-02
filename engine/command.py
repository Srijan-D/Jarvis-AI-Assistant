import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('rate',174)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
    
@eel.expose
def takecommand():
    r=sr.Recognizer() #Creates a new recognizer instance, which can recognize speech.
    with sr.Microphone() as source: #Opens the default microphone as the source of audio input.
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold=1 #Sets the amount of silence (in seconds) that will be considered as the end of a phrase.
        r.adjust_for_ambient_noise(source)#: Adjusts the recognizer sensitivity to the ambient noise.
        
        audio=r.listen(source,timeout=10,phrase_time_limit=6) #Listens for a single phrase, with a maximum wait time for speech (timeout) of 10 seconds and a maximum phrase length of 6 seconds.
        
    try:
        print("Recognizing...")
        eel.DisplayMessage("Listening...")
        query=r.recognize_google(audio,language='en-in') #Attempts to recognize what was said using Google's speech recognition service.
        print(f"User said: {query}")
        eel.DisplayMessage(query)    
        speak(query)
        eel.ShowHome()
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")
        return "None"    
    
    return query.lower()

