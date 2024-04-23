import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('rate',174)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()
speak("Hello, I am your ai assistant. How can I help you?")    