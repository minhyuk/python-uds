#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import can
import time
from struct import unpack

from uds import createUdsConnection
from uds import Uds

payload = []
test2Response = [0x62, 0xF1, 0x8C, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x30, 0x39]


# Callback function to handle the reception of a single-frame message and send a response
# Args:
#    msg: The message object received, which is expected to have 'arbitration_id' and 'data' attributes.
# 1. Optionally prints the received message ID and data (commented out lines).
# 2. Prepares a response message with predefined data.
# 3. Creates a new CAN message 'outMsg'.
# 4. Sets the 'arbitration_id' of 'outMsg' to 0x650.
# 5. Sets the 'data' of 'outMsg' to the prepared response data.
# 6. Sends 'outMsg' using 'bus1'.
# 7. Pauses execution for 1 second using 'time.sleep'.
def callback_onReceive_singleFrame(msg):
    #print("Received Id: " + str(msg.arbitration_id))
    #print("Data: " + str(msg.data))
    response = [0x04, 0x62, 0xF1, 0x8C, 0x01, 0x00, 0x00, 0x00]
    outMsg = can.Message()
    outMsg.arbitration_id = 0x650
    outMsg.data = response
    bus1.send(outMsg)
    time.sleep(1)


# Callback function to handle the reception of multi-frame messages and send a response without block size (BS) limitation
# Args:
#    msg: The message object received, which is expected to have 'arbitration_id' and 'data' attributes.
# 1. Uses the global variable 'payload'.
# 2. Optionally prints the received message ID and data (commented-out lines).
# 3. Extracts the Network Protocol Control Information (N_PCI) from the first byte of the received message data.
# 4. Creates a new CAN message 'outMsg'.
# 5. Sets the 'arbitration_id' of 'outMsg' to 0x650.
# 6. Depending on the value of 'N_PCI':
#    a. If 'N_PCI' is 0 (first frame):
#       - Sets the data of 'outMsg' to the first 6 bytes of 'test2Response' (response data).
#       - Sends 'outMsg' using 'bus1'.
#       - Pauses execution for 0.01 seconds.
#    b. If 'N_PCI' is 3 (consecutive frame):
#       - Sets the data of 'outMsg' to the next 7 bytes of 'test2Response'.
#       - Sends 'outMsg' using 'bus1'.
#       - Pauses execution for 0.01 seconds.
#       - Sets the data of 'outMsg' to the remaining bytes of 'test2Response' plus a padding byte [0].
#       - Sends 'outMsg' using 'bus1'.
#       - Pauses execution for 0.01 seconds.
def callback_onReceive_multiFrameResponse_noBs(msg):
    global payload
    # print("Received Id: " + str(msg.arbitration_id))
    # print("Data: " + str(msg.data))
    N_PCI = ((msg.data[0] & 0xf0) >> 4)
    outMsg = can.Message()
    outMsg.arbitration_id = 0x650
    if(N_PCI == 0):
        outMsg.data = [0x10, 19] + test2Response[0:6]
        bus1.send(outMsg)
        time.sleep(0.01)
    if(N_PCI == 3):
        outMsg.data = [0x21] + test2Response[6:13]
        bus1.send(outMsg)
        time.sleep(0.01)
        outMsg.data = [0x22] + test2Response[13:19] + [0]
        bus1.send(outMsg)
        time.sleep(0.01)

startTime = 0
lastTime = 0
# Callback function to handle the reception of multi-frame messages and send flow control responses
# Args:
#    msg: The message object received, which is expected to have 'arbitration_id' and 'data' attributes.
# 1. Uses global variables 'startTime' and 'lastTime'.
# 2. Records the current start time using 'time.time()'.
# 3. Optionally prints the separation time, received message ID, and data (commented-out lines).
# 4. Extracts the Network Protocol Control Information (N_PCI) from the first byte of the received message data.
# 5. Initializes 'responsePayload' as an empty list.
# 6. Creates a new CAN message 'outMsg'.
# 7. Sets the 'arbitration_id' of 'outMsg' to 0x650.
# 8. Depending on the value of 'N_PCI':
#    a. If 'N_PCI' is 1 (first frame):
#       - Prepares a flow control (FC) message with clear to send (CTS) parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
#    b. If 'N_PCI' is 2 (consecutive frame):
#       - Checks if the last byte of the received data is equal to 40, 110, or 180 (end of block).
#       - If true, prepares a FC message with CTS parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
# 9. Updates 'lastTime' with the recorded 'startTime'.

def callback_onReceive_multiFrameSend(msg):
    global startTime, lastTime
    startTime = time.time()
    #print("Separation time: " + str(startTime - lastTime))
    # print("Received Id: " + str(msg.arbitration_id))
    #print("Data: " + str(msg.data))
    response = msg.data
    N_PCI = (response[0] & 0xF0) >> 4
    responsePayload = []
    outMsg = can.Message()
    outMsg.arbitration_id = 0x650
    if(N_PCI == 1):
        #print("First frame received, responding CTS")
        responsePayload = [0x30, 5, 5, 00, 00, 00, 00, 00]
        outMsg.data = responsePayload
        bus1.send(outMsg)
    elif(N_PCI == 2):
        #print("Consecutive frame received")
        if(
                (msg.data[7] == 40) |
                (msg.data[7] == 110) |
                (msg.data[7] == 180)
        ):
            #print("End of block, sending CTS")
            responsePayload = [0x30, 10, 10, 00, 00, 00, 00, 00]
            outMsg.data = responsePayload
            bus1.send(outMsg)
    lastTime = startTime

# Callback function to handle the reception of multi-frame messages and send flow control responses with optional wait indications
# Args:
#    msg: The message object received, which is expected to have 'arbitration_id' and 'data' attributes.
# 1. Prints the received message ID and data (unpacks the data for better readability).
# 2. Extracts the Network Protocol Control Information (N_PCI) from the first byte of the received message data.
# 3. Initializes 'responsePayload' as an empty list.
# 4. Creates a new CAN message 'outMsg'.
# 5. Sets the 'arbitration_id' of 'outMsg' to 0x650.
# 6. Depending on the value of 'N_PCI':
#    a. If 'N_PCI' is 1 (first frame):
#       - Prepares a flow control (FC) message with clear to send (CTS) parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
#    b. If 'N_PCI' is 2 (consecutive frame):
#       - Checks if the last byte of the received data is equal to 40, 75, 145, or 180 (end of block).
#       - If true, prepares a FC message with CTS parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
#       - If the last byte of the received data is 110, prepares a FC message with a wait indication (WT).
#       - Sets the data of 'outMsg' to 'responsePayload' and sends it using 'bus1'.
#       - Pauses execution for 0.7 seconds.
#       - Prepares another FC message with CTS parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload' and sends it using 'bus1'.

def callback_onReceive_multiFrameWithWait(msg):
    print("Received Id: " + str(msg.arbitration_id))
    print("Data: " + str(unpack('BBBBBBBB', msg.data)))
    response = msg.data
    N_PCI = (response[0] & 0xF0) >> 4
    responsePayload = []
    outMsg = can.Message()
    outMsg.arbitration_id = 0x650
    if(N_PCI == 1):
        #print("First frame received, responding CTS")
        responsePayload = [0x30, 5, 20, 00, 00, 00, 00, 00]
        outMsg.data = responsePayload
        bus1.send(outMsg)
    elif(N_PCI == 2):
        #print("Consecutive frame received")
        if(
                (msg.data[7] == 40) |
                (msg.data[7] == 75) |
                (msg.data[7] == 145) |
                (msg.data[7] == 180)
        ):
            #print("End of block, sending CTS")
            responsePayload = [0x30, 10, 10, 00, 00, 00, 00, 00]
            outMsg.data = responsePayload
            bus1.send(outMsg)
        elif( msg.data[7] == 110 ):
            #print("End of block, producing a Wait")
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x30, 10, 10, 00, 00, 00, 00, 00]
            outMsg.data = responsePayload
            bus1.send(outMsg)

# Callback function to handle the reception of multi-frame messages and send flow control responses with multiple wait indications
# Args:
#    msg: The message object received, which is expected to have 'arbitration_id' and 'data' attributes.
# 1. Uses global variables 'startTime' and 'lastTime'.
# 2. Records the current start time using 'time.time()'.
# 3. Optionally prints the separation time, received message ID, and data (commented-out lines).
# 4. Extracts the Network Protocol Control Information (N_PCI) from the first byte of the received message data.
# 5. Initializes 'responsePayload' as an empty list.
# 6. Creates a new CAN message 'outMsg'.
# 7. Sets the 'arbitration_id' of 'outMsg' to 0x650.
# 8. Depending on the value of 'N_PCI':
#    a. If 'N_PCI' is 1 (first frame):
#       - Prepares a flow control (FC) message with clear to send (CTS) parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
#    b. If 'N_PCI' is 2 (consecutive frame):
#       - Checks if the last byte of the received data is equal to 40, 75, 145, or 180 (end of block).
#       - If true, prepares a FC message with CTS parameters in 'responsePayload' and maximum separation time.
#       - Sets the data of 'outMsg' to 'responsePayload'.
#       - Sends 'outMsg' using 'bus1'.
#       - If the last byte of the received data is 110, prepares multiple FC messages with a wait indication (WT).
#       - Sets the data of 'outMsg' to 'responsePayload' and sends it using 'bus1'.
#       - Pauses execution for 0.7 seconds. Repeats this process four more times to simulate prolonged waiting.
#       - Finally, prepares another FC message with CTS parameters in 'responsePayload'.
#       - Sets the data of 'outMsg' to 'responsePayload' and sends it using 'bus1'.
# 9. Updates 'lastTime' with the recorded 'startTime'.

def callback_onReceive_multiFrameWith4Wait(msg):
    global startTime
    global lastTime
    startTime = time.time()
    #print("Separation time: " + str(startTime-lastTime))
    #print("Received Id: " + str(msg.arbitration_id))
    #print("Data: " + str(msg.data))
    response = msg.data
    N_PCI = (response[0] & 0xF0) >> 4
    responsePayload = []
    outMsg = can.Message()
    outMsg.arbitration_id = 0x650
    if(N_PCI == 1):
        #print("First frame received, responding CTS")
        responsePayload = [0x30, 5, 5, 00, 00, 00, 00, 00]
        outMsg.data = responsePayload
        bus1.send(outMsg)
    elif(N_PCI == 2):

        #print("Consecutive frame received")
        if(
                (msg.data[7] == 40) |
                (msg.data[7] == 75) |
                (msg.data[7] == 145) |
                (msg.data[7] == 180)
        ):
            #print("End of block, sending CTS")
            responsePayload = [0x30, 10, 127, 00, 00, 00, 00, 00]
            outMsg.data = responsePayload
            bus1.send(outMsg)
        elif( msg.data[7] == 110 ):
            #print("End of block, producing a Wait")
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x31, 0, 0, 0, 0, 0, 0, 0]
            outMsg.data = responsePayload
            bus1.send(outMsg)
            time.sleep(0.7)
            responsePayload = [0x30, 10, 127, 00, 00, 00, 00, 00]
            outMsg.data = responsePayload
            bus1.send(outMsg)
    lastTime = startTime


if __name__ == "__main__":
    bus1 = can.interface.Bus('virtualInterface', bustype="virtual")
    listener = can.Listener()
    notifier = can.Notifier(bus1, [listener], 0)

    uds = Uds(reqId=0x600, resId=0x650, interface="virtual")

    testEcu = createUdsConnection('Bootloader.odx', 'bootloader', interface="virtual")

    print("Test 1")
    listener.on_message_received = callback_onReceive_singleFrame
    resp = uds.send([0x22, 0xF1, 0x8C])
    print(resp)

    time.sleep(1)

    print("Test 2")
    listener.on_message_received = callback_onReceive_multiFrameResponse_noBs
    a = testEcu.readDataByIdentifier('ECU Serial Number')
    print(a)

    time.sleep(1)

    # print("Test 3")
    # listener.on_message_received = callback_onReceive_multiFrameSend
    # payloadRequest = []
    # for i in range(0, 200):
    #     payloadRequest.append(i)
    # udsMsg.request = payloadRequest
    # udsMsg.responseRequired = False
    # uds.send(udsMsg)
    # time.sleep(1)

    # print("Test 4")
    # listener.on_message_received = callback_onReceive_multiFrameWithWait
    # payloadRequest = []
    # for i in range(0, 200):
    #     payloadRequest.append(i)
    # udsMsg.request = payloadRequest
    # udsMsg.responseRequired = False
    # uds.send(udsMsg)

    # print("Test 5")
    # listener.on_message_received = callback_onReceive_multiFrameWith4Wait
    # payloadRequest = []
    # for i in range(0, 200):
    #     payloadRequest.append(i)
    # udsMsg.request = payloadRequest
    # udsMsg.responseRequired = False
    # uds.send(udsMsg)