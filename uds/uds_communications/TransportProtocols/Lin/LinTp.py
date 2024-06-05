"""
This module defines the LinTp class which supports the LIN transport protocol.

Attributes:
    iTp: Base class for transport protocol interfaces.
    Config: Class for handling configuration options.
    ResettableTimer: Class for timing control.
    fillArray: Function for padding an array.
    LinTpState: Enumeration of the state of LinTp.
    LinTpMessageType: Enumeration of types of messages in LinTp.
    LINTP_MAX_PAYLOAD_LENGTH: Constant for the maximum payload length.
    N_PCI_INDEX: Constant for the index of N_PCI.
    SINGLE_FRAME_DL_INDEX: Constant for the index of single frame DL.
    SINGLE_FRAME_DATA_START_INDEX: Constant for the starting index of single frame data.
    FIRST_FRAME_DL_INDEX_HIGH: Constant for the index of first frame DL high nibble.
    FIRST_FRAME_DL_INDEX_LOW: Constant for the index of first frame DL low nibble.
    FIRST_FRAME_DATA_START_INDEX: Constant for the starting index of first frame data.
    CONSECUTIVE_FRAME_SEQUENCE_NUMBER_INDEX: Constant for the index of consecutive frame sequence number.
    CONSECUTIVE_FRAME_SEQUENCE_DATA_START_INDEX: Constant for the starting index of consecutive frame sequence data.

Functions:
    - LinTp: Main class supporting LIN transport protocol.
    - send: Sends data over LIN.
    - recv: Receives data over LIN.
    - closeConnection: Closes the LIN connection.
    - clearBufferedMessages: Clears the receive buffer for messages.
    - getNextBufferedMessage: Retrieves the next message from the receive buffers.
    - create_blockList: Creates a list of data blocks based on block size and payload.
"""
