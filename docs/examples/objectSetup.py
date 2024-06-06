"""
This script demonstrates the use of the Uds class from the uds module to interact with an ECU. It shows how to create Uds objects, send requests, and handle responses.

- An Uds object `odxEcu` is created from the "Bootloader.odx" file using the `createUdsConnection` method with an empty string and the interface specified as "peak".
- A request for the ECU Serial Number is sent using the `readDataByIdentifier` method, and the result is stored in `esn`.
- The ASCII string obtained is printed.
- Another Uds object `rawEcu` is created manually using specific request and response IDs (0x7E0 and 0x7E8) and the interface "peak".
- A request for the ECU Serial Number is sent using the `send` method with the payload [0x22, 0xF1, 0x8C], and the raw payload returned is stored in `esnRaw`.
- The raw payload returned from the ECU is printed.

This script showcases the usage of the Uds class to interact with ECUs using different methods and configurations.
"""
import uds 
from uds import Uds

if __name__ == "__main__":
    # Script logic for interacting with an ECU using Uds objects
    # ...
