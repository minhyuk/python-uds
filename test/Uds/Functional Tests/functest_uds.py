"""
This script demonstrates the usage of the Uds class in performing single-frame and multi-frame responses in the context of
Unified Diagnostic Services (UDS) protocol implementation. The script initializes a virtual bus 'virtualInterface' using the
Bus class from the can library. Several functions are defined to manage message reception, including clearing the receive buffer,
getting the next received message from the buffer, and handling incoming messages.

Two main functions are implemented to simulate UDS responses: singleFrameResponse_target and multiFrameResponse_target. The
singleFrameResponse_target function constructs and sends a CAN message with a single-frame UDS response after a certain time period.
The multiFrameResponse_target function sends multi-frame UDS responses based on the received messages within a specified duration.

In the main block, a Listener and Notifier are set up to handle incoming messages on the bus. Instances of the Uds class are created,
and two tests are conducted: Test 1 for single-frame response and Test 2 for multi-frame response. Threads are used to simulate
concurrent processing of UDS requests and responses. The script executes the tests and prints the results accordingly in a controlled
manner.
"""
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


def clearReceiveBuffer():
    global recvBuffer
    recvBuffer = []


def getNextReceivedMessage():
    global recvBuffer
    if len(recvBuffer) == 0:
        return None
    else:
        return recvBuffer.pop(0)

def onReceiveCallback(msg):
    global recvBuffer
    recvBuffer.append(msg.data)

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
