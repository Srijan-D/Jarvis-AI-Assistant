import os
import eel

    
eel.init("frontend")



os.system('start msedge.exe --app="http://localhost:8000/index.html"')   
# this opens the browser with the localhost server

eel.start('index.html', mode=None, host='localhost', block=True)
# this starts server at localhost and serves the index.html file