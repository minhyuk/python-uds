from uds import Uds
from can import Bus, Listener, Notifier
from time import sleep

# Function to handle the receiving callback with specific arbitration ID checks
# Args:
#    msg: The message object received, which is expected to have 'data' and 'arbitration_id' attributes.
#     - data: The payload of the message.
#     - arbitration_id: The ID of the message.
# Checks the arbitration ID of the received message and prints the data 
# with a specific message depending on the ID.
# ID 0x600: Bootloader message
# ID 0x7E0: PCM message
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

