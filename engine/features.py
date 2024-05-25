import os
from pipes import quote
import re
import sqlite3
import struct
import subprocess
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import pvporcupine

from engine.helper import extract_yt_term, remove_words

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
    

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
                                                                    
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"])  # pre trained keywords in
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

# find contacts
def findContact(query):
    
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])

        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    # flag is used to determine the type of messsage/voice call/video call

    if flag == 'message':
        target_tab = 12 
        # after opening whatsapp, it takes 12 tabs(click on tab button) to reach the message box
        jarvis_message = "message send successfully to "+name

    elif flag == 'call':
        target_tab = 7
        # it takes 7 tabs to reach the call button
        message = ''
        jarvis_message = "calling to "+name

    else:
        target_tab = 6
        #  it takes 6 tabs to reach the video call button
        message = ''
        jarvis_message = "staring video call with "+name

    # Encode the message for URL 
    encoded_message = quote(message)
    print(encoded_message)
    #  Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the command to open WhatsApp with the URL
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    # called this twice because sometimes it doesn't open whatsapp in first attempt or takes some time to open
    
    pyautogui.hotkey('ctrl', 'f')
    # this click focuses on the search bar in whatsapp

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
        # press tab to reach the target tab number is passed as argument

    pyautogui.hotkey('enter') # press enter to send the message
    speak(jarvis_message)
    