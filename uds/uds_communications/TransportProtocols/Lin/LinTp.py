"""
This script contains a LinTp class that supports the LIN transport protocol. It transmits and receives messages over a LIN
bus. The class implements methods for sending and receiving data over LIN, with functionality to create block lists from
the block size and payload and handle the callback when a message is received.

Methods:
- __init__: Initializes the LinTp object and sets up the LIN connection.
- send: Sends a message over the LIN bus, handling the single frames, first frames, and consecutive frames logic.
- recv: Receives a message from the LIN bus.
- closeConnection: Closes the LIN bus connection.
- callback_onReceive: Handles the message received callback.
- clearBufferedMessages: Clears out the receive list.
- getNextBufferedMessage: Retrieves the next message from the received message buffers.
- create_blockList: Creates a block list from the block size and payload.
- transmit: Transmits the data over the LIN bus.
- wakeup: Wakes up the LIN bus if asleep.
- __loadConfiguration: Loads the configuration options and overrides them with any passed-in from a config file.
- __checkKwargs: Goes through the kwargs and overrides any of the local configuration options.
"""
