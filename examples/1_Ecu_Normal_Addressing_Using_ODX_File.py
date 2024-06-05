"""
This script demonstrates the usage of the 'createUdsConnection' function from the Uds library to establish a connection based on the provided ODX file and parameters.

1. It creates a Uds connection 'a' with the given ODX file 'Diagnostics.odx-d', request and response IDs (0x7E0 and 0x7E8 respectively), peak interface, and device 'PCAN_USBBUS1'.
2. Reads the ECU Serial Number by sending a request with the identifier "ECU Serial Number" and stores the result in 'SerialNumber'.
3. Prints the decoded serial number value, which is expected to be "000000000098" for the E400 ECU or similar.
"""
