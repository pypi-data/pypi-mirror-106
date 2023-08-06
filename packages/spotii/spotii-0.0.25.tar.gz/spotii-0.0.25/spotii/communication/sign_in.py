import json
import os
import requests
import threading
import time
import sys
import queue

from define import *

class SignIn(threading.Thread):
    def __init__(self, *args):             # self, imageFile, image-identifier, queue
        threading.Thread.__init__(self)
        self.notifyQue = args[0]
#qForGui format: [device_index, retCode, QRcode, message]
    def run(self):
        excReason=''
        for i in range(SIGN_IN_RETRY):
            try:
                service = "/signinlookspot"
                url = baseUrl + service
                payload = json.dumps({
                  "userid": "feng.gao@laipac.com",
                  "password": "123456"
                })
#                 payload = json.dumps({
#                   "userid": "cfzheng@biomyx.net",
#                   "password": "zheng11"
#                 })
                
                
                headers = {
                  'Authorization': 'Basic bGFpcGFjOmxhaXBhY3dz',
                  'Content-Type': 'application/json'
                }
                response = requests.request("POST", url, headers=headers, data=payload)
                print(response.text)
                parsing=json.loads(response.text)
                if parsing[CODE] == RESPONSE_SUCCESS:
                    self.notifyQue.put( [NON_SLOT_INDEX, SIGN_IN_SUCCESS, parsing[RSLT][TKEN], ''] )
                else:
                    self.notifyQue.put( [NON_SLOT_INDEX, SIGN_IN_FAIL,  parsing[CODE], parsing[DESC]] )
                return
            except Exception as e:
                excReason = "signInException"
                print(e)
            time.sleep(5)
            
        else:
            self.notifyQue.put( [NON_SLOT_INDEX, SIGN_IN_FAIL,  excReason, ''] )
            
def signIn_test():
    notifyQue=queue.Queue()
    signIn=SignIn(notifyQue)
    signIn.start()
    
    while True:
        notify = notifyQue.get()
        print(notify)
        notifyQue.task_done()
        time.sleep(0.1)
        if not signIn.is_alive():
            break;
    print("sign in done")
    

if __name__ == "__main__":
    signIn_test()    
