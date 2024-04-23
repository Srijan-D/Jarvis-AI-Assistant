# import playsound as playsound
from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dir="frontend\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)