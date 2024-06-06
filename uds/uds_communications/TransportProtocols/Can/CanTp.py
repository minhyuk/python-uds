"""
This script defines the CanTp class that supports the CAN transport protocol.
- CanTp: Support CAN transport protocol
    - __init__: Initialize the CanTp object with the configuration settings and parameters
    - send: Send the payload over the CAN connection
    - recv: Receive the payload from the CAN connection
    - closeConnection: Dummy function to close the connection
    - clearBufferedMessages: Clear the receive list
    - getNextBufferedMessage: Get the next message from the receive list
    - callback_onReceive: Listener callback when a message is received
    - decode_stMin: Decode the StMin parameter
    - create_blockList: Create blocklist from blocksize and payload
    - transmit: Transmit the data over the CAN using the CAN connection

Includes enumeration and configuration settings for the CAN transport protocol.
"""
