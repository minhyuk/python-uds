#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import can
from threading import Thread
from time import time, sleep
from uds import Uds


recvBuffer = []
bus = can.interface.Bus('virtualInterface', bustype='virtual')


# Function to clear the global receive buffer
# Uses the global variable 'recvBuffer' and empties its contents by assigning an empty list.
def clearReceiveBuffer():
    global recvBuffer
    recvBuffer = []


# Function to retrieve the next received message from the global receive buffer
# Uses the global variable 'recvBuffer'
# Returns:
#    - The next message from 'recvBuffer' if available, otherwise returns None.
#      The message is removed from the buffer once retrieved.
def getNextReceivedMessage():
    global recvBuffer
    if len(recvBuffer) == 0:
        return None
    else:
        return recvBuffer.pop(0)

# Function to handle the receiving callback and store the message data in the global receive buffer
# Args:
#    msg: The message object received, which is expected to have a 'data' attribute.
#     - data: The payload of the message to be appended to the global receive buffer.
# Uses the global variable 'recvBuffer' to store received message data.
def onReceiveCallback(msg):
    global recvBuffer
    recvBuffer.append(msg.data)

# Function to handle a single frame response for a target
# Uses global variables 'bus' and 'recvBuffer'.
# 1. Initializes a working loop and sets a start time.
# 2. Creates a CAN message with `arbitration_id` set to 0x650.
# 3. Clears the receive buffer to ensure no old messages are processed.
# 4. Enters a while loop that runs until either a message is received or 5 seconds elapse.
# 5. Continuously checks if the time elapsed is greater than 5 seconds to exit the loop.
# 6. Retrieves the next received message from the receive buffer.
# 7. If a message is received, sets the CAN message data and sends it,
#    then exits the loop.
def singleFrameResponse_target():

    global bus

    working = True
    startTime = time()

    canMsg = can.Message(arbitration_id=0x650)
    clearReceiveBuffer()

    while working:
        currTime = time()
        if (currTime - startTime) > 5:
            working = False

        recvMsg = getNextReceivedMessage()

        if recvMsg is not None:
            canMsg.data = [0x04, 0x62, 0xF1, 0x8C, 0x01]
            bus.send(canMsg)
            working = False

# Function to handle a multi-frame response for a target
# Uses global variables 'bus' and 'recvBuffer'.
# 1. Initializes a working loop, sets a start time, and creates a CAN message with `arbitration_id` set to 0x650.
# 2. Clears the receive buffer to ensure no old messages are processed.
# 3. Sets an index to track message parts and a flag 'response' to monitor received messages.
# 4. Enters a while loop that runs until either a message is received and processed or 50 seconds elapse.
# 5. Continuously checks if the time elapsed is greater than 50 seconds to exit the loop.
# 6. Retrieves the next received message from the receive buffer.
# 7. Sets the response flag to True if a message is received.
# 8. If the response flag is True, sends the proper sequence of CAN messages:
#    - For the initial frame (index == 0), sends the first part of the multi-frame message, then increments the index.
#    - For the first consecutive frame (index == 1), sends the second part of the multi-frame message, then increments the index.
#    - For the second consecutive frame (index == 2), sends the third part of the multi-frame message, then exits the loop.
# 9. After sending each part, waits for 20 milliseconds before proceeding.
def multiFrameResponse_target():

    global bus

    working = True
    startTime = time()

    canMsg = can.Message(arbitration_id=0x650)
    clearReceiveBuffer()

    index = 0

    response = False

    while working:
        currTime = time()
        if (currTime - startTime) > 50:
            working = False

        recvMsg = getNextReceivedMessage()

        if recvMsg is not None:
            response = True

        if response:
            if index == 0:
                sleep(0.002)
                canMsg.data = [0x10, 0x13, 0x62, 0xF1, 0x8C, 0x30, 0x30, 0x30]
                index = 1
            elif index == 1:
                canMsg.data = [0x21, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30]
                index = 2
            elif index == 2:
                canMsg.data = [0x22, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x00]
                working = False

            bus.send(canMsg)
            sleep(0.020)


if __name__ == "__main__":

    listener = can.Listener()
    notifier = can.Notifier(bus, [listener], 0)

    listener.on_message_received = onReceiveCallback

    udsConnection = Uds()

    print("Test 1")
    clearReceiveBuffer()
    receiveThread = Thread(target=singleFrameResponse_target)
    receiveThread.start()
    sleep(0.2)
    a = udsConnection.send([0x22, 0xF1, 0x8C])
    print(a)

    while(receiveThread.is_alive()):
        pass

    print("Test 2")
    clearReceiveBuffer()
    receiveThread = Thread(target=multiFrameResponse_target)
    receiveThread.start()
    a = udsConnection.send([0x22, 0xF1, 0x8C])
    print(a)

    while(receiveThread.is_alive()):
        pass
