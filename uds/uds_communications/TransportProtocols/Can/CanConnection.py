"""
This script defines the CanConnection class to manage multiple clients for each bus or connection.
- CanConnection: Manage the CAN Bus/Notifier/Listeners to allow multiple clients for each bus/connection.
    - __init__: Initialize the CanConnection object with the callback, filter, and bus.
    - addCallback: Add a callback (via an additional listener) to the notifier attached to this bus.
    - addFilter: Add a filter (CAN Msg Id) to the bus to allow messages through to the callback.
    - transmit: Transmit the data over the CAN using the CanConnection.
"""
