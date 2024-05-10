# import playsound as playsound
import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
@eel.expose
def playAssistantSound():
    music_dir="frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"") # Remove JARVIS from query
    query=query.replace("open","") #remove open from the query by user
    query.lower()
    
    if query!="":
        speak("Opening "+query)
        os.system('start'+query) #open the file using os module start brave or start chrome
    else:
        speak("not found")       

def playYoutube(query):
    search_query=extract_yt_term(query)
    speak("Playing "+search_query+" on youtube")
    kit.playonyt(search_query) #play on youtube
    

def extract_yt_term(command):
    # Regex to find song name 
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    match=re.search(pattern,command,re.IGNORECASE)
    # if match found return song name
    return match.group(1) if match else None