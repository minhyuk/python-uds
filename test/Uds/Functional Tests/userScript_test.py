"""
This script illustrates the usage of the Uds class to send data using Unified Diagnostic Services (UDS) protocol. It also
utilizes the Bus, Listener, and Notifier classes from the can library. The callback function, callback_onReceive, is defined
to print the received message data based on the arbitration ID. If the arbitration ID is 0x600, it prints as "Bootloader Receive",
and if it is 0x7E0, it prints as "PCM Receive".

In the main block, a virtual bus 'virtualInterface' is initialized using the Bus class with 'virtual' as the bustype. A listener
is set up with its on_message_received attribute assigned to the callback_onReceive function. A Notifier is created with the
listener and the receive bus. An instance of the Uds class is then used to send a UDS request with a specific payload [0x22, 0xf1, 0x8C].
After sending the request, the script pauses for 2 seconds using the sleep function before finishing the execution.
"""
from uds import Uds
from can import Bus, Listener, Notifier
from time import sleep

def callback_onReceive(msg):

    if(msg.arbitration_id == 0x600):
        print("Bootloader Receive:", list(msg.data))
    if(msg.arbitration_id == 0x7E0):
        print("PCM Receive:", list(msg.data))


if __name__ == "__main__":

    recvBus = Bus("virtualInterface", bustype="virtual")

    listener = Listener()
    notifier = Notifier(recvBus, [listener], 0)

    listener.on_message_received = callback_onReceive

    a = Uds()

    a.send([0x22, 0xf1, 0x8C], responseRequired=False)

    sleep(2)
