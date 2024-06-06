"""
This script demonstrates the usage of Uds class to send data using Unified Diagnostic Services (UDS) protocol. It imports
the Uds class along with Notifier and Listener classes from the respective modules. Two callback functions, onCallback_receive
and onCallback_receive2, are defined to handle received messages on different buses. The script initializes two virtual
buses ('virtualInterface' and 'anotherBus') using the can library and sets up listeners with the corresponding callback functions
to receive messages.

Instances of the Uds class are created and used to send UDS requests with specified payloads to different configurations. Various
scenarios are tested, including sending requests with different initialization files, custom request and response identifiers,
and handling exceptions.

After sending the UDS requests, the script enters a sleep state for 1 second before finishing the execution. Overall, this script
is a comprehensive example showcasing the usage of Uds class for interacting with UDS protocol and handling message reception on
different virtual buses.
"""
from uds import Uds
from can import Notifier, Listener
import can
from time import sleep


def onCallback_receive(msg):
    print("Received: {0} on ID: {1} on virtualInterface".format(list(msg.data), hex(msg.arbitration_id)))
    pass


def onCallback_receive2(msg):
    print("Received: {0} on ID: {1} on anotherBus".format(list(msg.data), hex(msg.arbitration_id)))
    pass


if __name__ == "__main__":

    bus = can.interface.Bus('virtualInterface', bustype='virtual')
    bus2 = can.interface.Bus('anotherBus', bustype='virtual')

    listener = Listener()
    listener.on_message_received = onCallback_receive
    notifier = Notifier(bus, [listener], 0)

    listener2 = Listener()
    listener2.on_message_received = onCallback_receive2
    notifier2 = Notifier(bus2, [listener2], 0)

    a = Uds()
    a.send([0x22, 0xF1, 0x8C], responseRequired=False)

    b = Uds("bootloader.ini")
    b.send([0x22, 0xF1, 0x80], responseRequired=False)

    c = Uds("bootloader2.ini")
    c.send([0x22, 0xF1, 0x81], responseRequired=False)

    try:
        d = Uds("subaruEcm.ini")
    except:
        print("Subaru ECM test passed, using doip, exception caught")

    e = Uds(reqId=0x620, resId=0x670)
    e.send([0x22, 0xf1, 0x83], responseRequired=False)

    sleep(1)
