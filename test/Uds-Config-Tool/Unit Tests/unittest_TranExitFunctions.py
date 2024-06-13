#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import unittest
from unittest import mock
from uds import Uds
from uds.uds_config_tool.UdsConfigTool import createUdsConnection
import sys, traceback


class TransferExitTestCase(unittest.TestCase):

    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer exit request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer exit request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferExit method to transferExit in the Uds object.
    # 4. Calls the 'transferExit' method on the Uds connection object with the specified parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferExit method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x37] followed by the parameter record, and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'transferExit' is a dictionary containing:
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transExitRequest(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x77, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferExit to transferExit in the uds object, so can now call below
    
            b = a.transferExit([0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferExit, which does the Uds.send - takes blockSequenceCounter and parameterRecord
            canTp_send.assert_called_with([0x37, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual({'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the transfer exit request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferExit method to transferExit in the Uds object.
    # 4. Attempts to call the 'transferExit' method on the Uds connection object with the specified parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferExit method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x37] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    #    - Indicates that transferExit should not return a value when a negative response is detected.
    
    def test_transExitNegResponse_0x13(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferExit to transferExit in the uds object, so can now call below
    
            try:
                b = a.transferExit([0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferExit, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x37, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... transferExit should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the transfer exit request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferExit method to transferExit in the Uds object.
    # 4. Attempts to call the 'transferExit' method on the Uds connection object with the specified parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferExit method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x37] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    #    - Indicates that transferExit should not return a value when a negative response is detected.
    
    def test_transExitNegResponse_0x22(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferExit to transferExit in the uds object, so can now call below
    
            try:
                b = a.transferExit([0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferExit, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x37, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)  # ... transferExit should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x24) for the transfer exit request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x24.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferExit method to transferExit in the Uds object.
    # 4. Attempts to call the 'transferExit' method on the Uds connection object with the specified parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferExit method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x37] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x24']".
    #    - Indicates that transferExit should not return a value when a negative response is detected.
    
    def test_transExitNegResponse_0x24(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x24]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferExit to transferExit in the uds object, so can now call below
    
            try:
                b = a.transferExit([0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferExit, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x37, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x24']", b)  # ... transferExit should not return a value




if __name__ == "__main__":
    unittest.main()