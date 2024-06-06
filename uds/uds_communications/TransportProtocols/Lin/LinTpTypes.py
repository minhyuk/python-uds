"""
This script defines some LinTpState enums and LinTpMessageType enums for the LIN transport protocol. It also provides 
constants for the maximum payload length and relevant indexes for various components of LIN frames.

Enums:
- LinTpState: Enum for defining the state of the LIN transport protocol, including IDLE, SEND_SINGLE_FRAME, 
SEND_FIRST_FRAME, SEND_CONSECUTIVE_FRAME, and RECEIVING_CONSECUTIVE_FRAME.
- LinTpMessageType: IntEnum for defining types of LIN frames, including SINGLE_FRAME, FIRST_FRAME, and CONSECUTIVE_FRAME.

Constants:
- LINTP_MAX_PAYLOAD_LENGTH: Maximum payload length for LIN frames.
- N_PCI_INDEX: Index for identifying the PCI byte in LIN frames.
- SINGLE_FRAME_DL_INDEX: Index for single frame data length in LIN frames.
- SINGLE_FRAME_DATA_START_INDEX: Starting index for single frame data in LIN frames.
- FIRST_FRAME_DL_INDEX_HIGH: High index for first frame data length in LIN frames.
- FIRST_FRAME_DL_INDEX_LOW: Low index for first frame data length in LIN frames.
- FIRST_FRAME_DATA_START_INDEX: Starting index for first frame data in LIN frames.
- CONSECUTIVE_FRAME_SEQUENCE_NUMBER_INDEX: Index for consecutive frame sequence number in LIN frames.
- CONSECUTIVE_FRAME_SEQUENCE_DATA_START_INDEX: Starting index for consecutive frame sequence data in LIN frames.
"""
