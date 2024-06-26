import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    text=str(text)
    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('rate',174)
    engine.setProperty('voice',voices[1].id)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text) # text spoken by the assistant
    engine.runAndWait()
    
@eel.expose
def takecommand():
    r=sr.Recognizer() #Creates a new recognizer instance, which can recognize speech.
    with sr.Microphone() as source: #Opens the default microphone as the source of audio input.
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold=1 #Sets the amount of silence (in seconds) that will be considered as the end of a phrase.
        r.adjust_for_ambient_noise(source)#: Adjusts the recognizer sensitivity to the ambient noise.
        audio=r.listen(source,timeout=4,phrase_time_limit=2) #Listens for a single phrase, with a maximum wait time for speech (timeout) of 10 seconds and a maximum phrase length of 6 seconds.
        
    try:
        print("Recognizing...")
        eel.DisplayMessage("Listening...")
        query=r.recognize_google(audio,language='en-in') #Attempts to recognize what was said using Google's speech recognition service.
         
        print(f"User said: {query}")
        eel.DisplayMessage(query)    
        speak(query)
    
    except Exception as e:
        print(e)
        print("Say that again please...")
        eel.DisplayMessage("Say that again please...")
        return "None"    
    
    return query.lower()

@eel.expose
def allCommands(message=1):
    
    if message==1:
        query=takecommand()
        print(query)
        eel.senderText(query)
        # message from the user
        
    else:
        query=message    
        eel.senderText(query)
   
    try:
        # open feature in features.py
        if "open" in query:
            print("Opening "+query)
            from engine.features import openCommand
            openCommand(query)
            
        # youtube feature in features.py
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query) 
        
        # whatsapp feature in features.py
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message would you like to send?")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                    
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)     
            
        else:
            print("Not opening passing to huggingface model")
            from engine.features import chatBot
            chatBot(query)
    except:
        print("Error")    
           
    eel.ShowHome()  
