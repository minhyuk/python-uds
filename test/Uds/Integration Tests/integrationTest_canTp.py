#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


from threading import Thread
from uds import CanTp
from time import sleep


if __name__ == "__main__":

    sender = CanTp(reqId=0x600, resId=0x650)

    # Function to receive a message using the CanTp transport protocol and print the length of the received message
    # 1. Initializes a CanTp receiver with request ID 0x650 and response ID 0x600.
    # 2. Calls the 'recv' method on the receiver to receive a message with a timeout of 100 milliseconds.
    # 3. Prints the length of the received message.
    def receiverFunc():
    
            receiver = CanTp(reqId=0x650, resId=0x600)
    
            a = receiver.recv(100)
    
            #print(a)
            print(len(a))

    receiverThread = Thread(target=receiverFunc)

    payload = []
    for i in range(1, 4095):
        payload.append(i % 0xFF)

    receiverThread.start()
    sleep(0.2)
    sender.send(payload)

    sleep(1)
