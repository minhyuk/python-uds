"""
This script defines a 'fillArray' function and the 'TestTp' class supporting a test transport protocol.
The 'fillArray' function pads out an array with a fill value.

Class Details:
- Name: TestTp
- Description: Main class to support the Test transport protocol
- For incoming messages, it will spawn a CanTpListener class
- It depends on a bus object for communication on CAN

Methods:
- send: Indicates the method for sending, raises an exception that the Test send should not be used directly, only mocked
- recv: Indicates the method for receiving, raises an exception that the Test receive should not be implemented directly, only mocked
"""
