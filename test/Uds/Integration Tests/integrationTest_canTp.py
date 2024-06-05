"""
This script demonstrates a simple scenario with a sender and receiver communicating over a CanTp (CAN Transport Protocol) connection. The main block initializes a CanTp instance for the sender and spawns a separate thread to handle the receiving functionality through another instance of CanTp. The receiver function (receiverFunc) is defined to receive a maximum of 100 bytes of data and prints the length of the received data. The sender generates a payload of data and sends it using the sender CanTp instance. Multithreading is utilized to concurrently run the sender and receiver activities, with a delay introduced for synchronization before the program exits after 1 second.
"""
