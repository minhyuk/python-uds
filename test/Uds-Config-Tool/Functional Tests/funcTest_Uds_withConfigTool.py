"""
This script sets up a virtual CAN bus and listener to simulate UDS communication for testing purposes. It utilizes different callbacks to handle different types of received messages: single-frame, multi-frame response without BlockSize negotiation, multi-frame response with BlockSize negotiation.

1. Test 1: Sends a single-frame request to the UDS device and expects a specific single-frame response. It uses the `callback_onReceive_singleFrame` callback for handling the received message.

2. Test 2: Requests ECU Serial Number from the vehicle's bootloader using UDS communication and expects a multi-frame response without BlockSize negotiation. It employs the `callback_onReceive_multiFrameResponse_noBs` callback for processing the response.

3. Test 3: (Commented Out) Demonstrates sending a multi-frame request with BlockSize negotiation. It uses the `callback_onReceive_multiFrameSend` callback which handles the response message.

4. Test 4: (Commented Out) Illustrates receiving a multi-frame response (with BlockSize negotiation) and waiting for acknowledgment before sending the next frame. Uses the `callback_onReceive_multiFrameWithWait` callback technique.

5. Test 5: (Commented Out) Shows handling a multi-frame response with multiple waits for acknowledgments before sending the next frame. Utilizes the `callback_onReceive_multiFrameWith4Wait` callback method.
"""
