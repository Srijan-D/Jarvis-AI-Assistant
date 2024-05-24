import multiprocessing

def startJarvis():
    # process to start jarvis
    print("Starting process 01")
    from main import start
    start()
    
    # process to start hotword detection
def hotwordDetection():
    print("Starting process 02")
    from engine.features import hotword
    hotword()    
    
    
if __name__ == '__main__':
    # creating process
    p1=multiprocessing.Process(target=startJarvis)
    p2=multiprocessing.Process(target=hotwordDetection)
    p1.start()
    p2.start()
    p1.join()
    
    if p2.is_alive():
        p2.terminate()
        p2.join()
        
    print("All processes are done")   