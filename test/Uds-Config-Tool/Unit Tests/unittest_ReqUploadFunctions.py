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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: these tests cannot currently be run with the exsiting ODX, as it does not contain an upload service
# For now, I've simply run a regression of the download and transfer tests to ensure I've not broken anything.
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class RequestUploadTestCase(unittest.TestCase):
	
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the request upload service
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the request upload.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Calls the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'requestUpload' is a dictionary with the correct keys and values:
    #    - 'LengthFormatIdentifier' with the value [0x20].
    #    - 'MaxNumberOfBlockLength' with the value [0x05, 0x00].
    
    def test_reqUploadRequest(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x74, 0x20, 0x05, 0x00]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x40, 0x03, 0xE0, 0x00], MemorySize=[0x00, 0x00, 0x0E, 0x56])	# ... calls __requestUpload, which does the Uds.send
    	
            canTp_send.assert_called_with([0x34, 0x00, 0x44, 0x40, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x0E, 0x56], False)
            self.assertEqual({'LengthFormatIdentifier':[0x20],'MaxNumberOfBlockLength':[0x05, 0x00]}, b)  # ... requestUpload should return a dictionary



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the request upload service with a different set of parameters
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the request upload.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Calls the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'requestUpload' is a dictionary with the correct keys and values:
    #    - 'LengthFormatIdentifier' with the value [0x40].
    #    - 'MaxNumberOfBlockLength' with the value [0x01, 0x00, 0x05, 0x08].
    
    def test_reqUploadRequest02(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x74, 0x40, 0x01, 0x00, 0x05, 0x08]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x01, 0xFF, 0x0A, 0x80], MemorySize=[0x03, 0xFF])	# ... calls __requestUpload, which does the Uds.send
    	
            canTp_send.assert_called_with([0x34, 0x00, 0x24, 0x01, 0xFF, 0x0A, 0x80, 0x03, 0xFF], False)
            self.assertEqual({'LengthFormatIdentifier':[0x40],'MaxNumberOfBlockLength':[0x01, 0x00, 0x05, 0x08]}, b)  # ... requestUpload should return a dictionary



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the request upload service
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Attempts to call the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    #    - This method internally calls the __requestUpload method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    
    def test_reqUploadNegResponse_0x13(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            try:
                b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x40, 0x03, 0xE0, 0x00], MemorySize=[0x00, 0x00, 0x0E, 0x56])	# ... calls __requestUpload, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x34, 0x00, 0x44, 0x40, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x0E, 0x56], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... requestUpload should not return a value



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the request upload service
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Attempts to call the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    #    - This method internally calls the __requestUpload method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    
    def test_wdbiNegResponse_0x31(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            try:
                b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x40, 0x03, 0xE0, 0x00], MemorySize=[0x00, 0x00, 0x0E, 0x56])	# ... calls __requestUpload, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x34, 0x00, 0x44, 0x40, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x0E, 0x56], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)  # ... requestUpload should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x33) for the request upload service
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x33.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Attempts to call the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    #    - This method internally calls the __requestUpload method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x33']".
    
    def test_wdbiNegResponse_0x33(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x33]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            try:
                b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x40, 0x03, 0xE0, 0x00], MemorySize=[0x00, 0x00, 0x0E, 0x56])	# ... calls __requestUpload, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x34, 0x00, 0x44, 0x40, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x0E, 0x56], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x33']", b)  # ... requestUpload should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x70) for the request upload service
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x70.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and parses the request upload information, attaching the __requestUpload method to requestUpload in the Uds object.
    # 4. Attempts to call the 'requestUpload' method on the Uds connection object with the specified format identifier, memory address, and memory size.
    #    - This method internally calls the __requestUpload method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x34, followed by format identifier, memory address, and memory size] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x70']".
    
    def test_wdbiNegResponse_0x70(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x70]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __requestUpload to requestUpload in the uds object, so can now call below
    
            try:
                b = a.requestUpload(FormatIdentifier=[0x00], MemoryAddress=[0x40, 0x03, 0xE0, 0x00], MemorySize=[0x00, 0x00, 0x0E, 0x56])	# ... calls __requestUpload, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x34, 0x00, 0x44, 0x40, 0x03, 0xE0, 0x00, 0x00, 0x00, 0x0E, 0x56], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x70']", b)  # ... requestUpload should not return a value



if __name__ == "__main__":
    unittest.main()