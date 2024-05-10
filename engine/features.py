import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

con=sqlite3.connect('jarvis.db')
cursor=con.cursor()


@eel.expose
def playAssistantSound():
    music_dir="frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)
    
def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"") # Remove JARVIS from query
    query=query.replace("open","") #remove open from the query by user
    query.lower()
    app_name=query.strip() #remove white spaces
    
    if app_name !="":
        
        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results=cursor.fetchall()
            
            if len(results) !=0:
                speak("Opening1 "+app_name)
                os.startfile(results[0][0])
            
            elif len(results)==0:
                cursor.execute(
                    'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results=cursor.fetchall()
            
            if(len(results)!=0):
                speak("Opening2 "+app_name)
                webbrowser.open(results[0][0])     
            
            else:
                speak("Opening3 "+app_name)
                try:
                    os.system('start '+app_name)
                except:
                    speak("Sorry, I am not able to open "+app_name)           
        except:
            speak("Something went wrong, please try again")    

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