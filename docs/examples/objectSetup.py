"""
This script demonstrates the usage of the Uds library by creating Uds objects and sending requests to retrieve ECU serial number information using ODX files and raw payloads.

1. It creates a Uds object 'odxEcu' from the 'Bootloader.odx' file with the interface 'peak'.
2. Sends a request to retrieve the ECU Serial Number and stores the result.
3. Prints the extracted ECU Serial Number as an ASCII string.
4. Creates another Uds object 'rawEcu' manually with specific request and response IDs and the interface 'peak'.
5. Sends a custom request for the ECU Serial Number using the raw payload [0x22, 0xF1, 0x8C].
6. Prints the raw payload returned from the ECU.
"""
