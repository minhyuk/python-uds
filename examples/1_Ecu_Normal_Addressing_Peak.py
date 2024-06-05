"""
This script demonstrates the usage of the 'Uds' class from the Uds library to send specific requests and print the responses.

1. It creates a Uds object 'a' with the provided request ID (0x7E0), response ID (0x7E8), interface ('peak'), and device ('PCAN_USBBUS1').
2. Sends a standard Tester Present request [0x3E, 0x00] and stores the response in 'TesterPresent'.
3. Prints the expected response, which should be [0x7E, 0x00].
4. Sends a request for the ECU Serial Number [0x22, 0xF1, 0x8C] and stores the response in 'SerialNumber'.
5. Prints the received response, which may vary depending on the ECU but should start with [0x6E, 0xF1, 0x8C].
"""
