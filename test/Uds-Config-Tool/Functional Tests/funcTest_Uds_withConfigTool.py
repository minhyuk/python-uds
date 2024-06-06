"""
The script consists of functionalities related to sending and receiving messages over a virtual CAN interface using UDS (Unified Diagnostic Services) protocols for bootloader communication with an ECU (Electronic Control Unit).

Key features covered in the script include:

1. CAN Interface Configuration:
    - Setting up a virtual CAN interface "bus1" for communication.
    - Define message listeners and notifiers to handle incoming CAN messages.
  
2. UDS and Connection Setup:
    - Instantiating Uds object for handling UDS messaging with specific request and response IDs.
    - Creating a UDS connection for bootloader interactions using the provided ODX file "Bootloader.odx".
  
3. Message Handling Callbacks:
    - Implementing different callback functions for processing single-frame responses, multi-frame responses, multi-frame responses with wait, and multi-frame responses with multiple waits accordingly.
  
4. Test Cases Execution:
    - Conducting various test cases to simulate different scenarios of sending UDS requests and handling corresponding responses.
    - Test scenarios include sending single-frame requests, multi-frame responses, and testing with different payload configurations.

Overall, the script showcases the setup and execution of UDS communication scenarios over a virtual CAN interface, including handling different types of UDS requests and responses for bootloader operations with an ECU.
"""
#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import can
import time
from struct import unpack

from uds import createUdsConnection
from uds import Uds
"""
