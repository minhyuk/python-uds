"""
This script defines several enums and constants related to the CanTp protocol.
- N_Result: Defines the different result states for the CanTp communication.
- CanTpAddressingTypes: Defines the different addressing types for CanTp connections.
- CanTpState: Defines the various states of the send or receive method.
- CanTpMessageType: Defines the type of message for CanTp (Single Frame, First Frame, etc.).
- CanTpFsTypes: Defines types such as 'ContinueToSend', 'Wait', and 'Overflow' for flow control.
- CanTpMTypes: Defines the diagnostics types for CanTp (Diagnostics and Remote Diagnostics).
- CANTP_MAX_PAYLOAD_LENGTH: Maximum payload length based on the ISO 15765 standard.
- N_PCI_INDEX: Index for N_PCI in the message.
- SINGLE_FRAME_DL_INDEX: Index for single frame DL in the message.
- SINGLE_FRAME_DATA_START_INDEX: Starting index for data in a single frame.
- FIRST_FRAME_DL_INDEX_HIGH: Higher byte index for First Frame DL.
- FIRST_FRAME_DL_INDEX_LOW: Lower byte index for First Frame DL.
- FIRST_FRAME_DATA_START_INDEX: Starting index for data in a First Frame.
- FC_BS_INDEX: Flow Control block size index.
- FC_STMIN_INDEX: Flow Control separation time index.
- CONSECUTIVE_FRAME_SEQUENCE_NUMBER_INDEX: Index for the sequence number in a Consecutive Frame.
- CONSECUTIVE_FRAME_SEQUENCE_DATA_START_INDEX: Starting index for data in a Consecutive Frame.
- FLOW_CONTROL_BS_INDEX: Flow Control block size index.
- FLOW_CONTROL_STMIN_INDEX: Flow Control separation time index.
"""
