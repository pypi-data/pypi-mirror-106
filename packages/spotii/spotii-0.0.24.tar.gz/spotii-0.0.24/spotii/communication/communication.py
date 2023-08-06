import threading
import time
import queue
import sys

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#sys.path.append('/home/pi/gxf/python/spotii')
#sys.path.append('/home/pi/gxf/python/spotii/communication')
#from image_post import post
from communication.ln_web import sendToApi
from communication.sign_in import SignIn
from define import *

class CommunicationThread (threading.Thread):
    def __init__(self, threadID, name, qForCom, qForResult):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.qForCom=qForCom
        self.qForResult=qForResult
        
    def aiServer(self):
        while True:
            image=self.qForCom.get()            
            post(image, self.qForResult)
            self.qForCom.task_done()
        
    def webApi(self):
        notifyQue=queue.Queue()
        signIn=SignIn(notifyQue)
        signIn.start()
        
        passToken=''

        notify = notifyQue.get()
        if notify[1] == SIGN_IN_SUCCESS:
            passToken = notify[2]
        print(notify)
        notifyQue.task_done()
        signIn.join()
        print("sign in done")
        
    
        
        while True:
            image=self.qForCom.get()
            if image == CLOSE_NOW:
                break;
            #print('image')
            sendToApi(image, self.qForResult, passToken, ADDRESS)
            self.qForCom.task_done()
        
    def run(self):
        super().run()
        print("communication thread start.")
        #self.aiServer()
        self.webApi()
  
#################### Test ####################
def com_test():
    qForCom=queue.Queue()
    qForResult = queue.Queue()
    com=CommunicationThread(3,"communication",qForCom, qForResult)
    com.start()
    
    time.sleep(2)
    

if __name__ == "__main__":
    com_test()   
