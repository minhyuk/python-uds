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

"""
This script demonstrates the use of Uds class for UDS communication along with handling received messages using callback functions. It sets up two virtual buses, attaches listeners to each bus, and sends UDS requests using different configurations provided to Uds instances. Custom message handling functions onCallback_receive and onCallback_receive2 are defined for processing received messages on virtual buses "virtualInterface" and "anotherBus" respectively. Exception handling is also showcased when creating a Uds instance with specific initialization files. 
"""
