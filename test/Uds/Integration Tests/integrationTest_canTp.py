"""
The script sets up a sender and a receiver using the CanTp class for communication involving request and response IDs. The receiver's functionality
is defined within a separate function called receiverFunc, where the receiver waits to receive a data payload and prints the length of the received
data.

In the main block, a sender instance is created with request and response IDs defined. Payload data is generated and stored in a list for sending.
A separate thread is initialized for the receiver functionality, and the receiverThread is started to concurrently handle the reception of data.
After a short delay, the sender sends the generated payload to the receiver using the CanTp send method.

The script demonstrates a simple communication setup between a sender and receiver using the CanTp class in a threaded environment to illustrate
data transmission and reception operations. The receiver function waits to receive a data payload while the sender sends the data, showcasing a basic
example of communication flow with concurrent processing using threads.
"""
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

    # Setting up sender and receiver
    sender = CanTp(reqId=0x600, resId=0x650)

    def receiverFunc():
        # Define receiver functionality
        receiver = CanTp(reqId=0x650, resId=0x600)

        # Receive and print the length of the received data
        a = receiver.recv(100)
        print(len(a))

    # Create a thread for receiver function
    receiverThread = Thread(target=receiverFunc)

    # Generate payload data for sending
    payload = []
    for i in range(1, 4095):
        payload.append(i % 0xFF)

    # Start the receiver thread and send the payload using the sender
    receiverThread.start()
    sleep(0.2)
    sender.send(payload)

    sleep(1)
"""
