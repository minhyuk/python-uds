"""
This module provides a factory class to create various types of CAN connection objects based on the configuration parameters.

The different connection types supported are:
- virtual: For virtual bus
- peak: For Peak devices
- vector: For Vector devices
- socketcan: For SocketCAN bus on Linux

The factory class provides a definition that reads the configuration, generates the connection objects based on the selected connection type and additional parameters provided.
"""
