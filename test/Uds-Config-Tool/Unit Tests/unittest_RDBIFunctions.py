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


class RDBITestCase(unittest.TestCase):
		
    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the read data by identifier (RDBI) for a single DID with an ASCII response
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response with the ECU Serial Number "ABC0011223344556".
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Calls the 'readDataByIdentifier' method on the Uds connection object.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'readDataByIdentifier' is a dictionary with the key 'ECU Serial Number' and the expected ASCII value "ABC0011223344556".
    def test_rdbiSingleDIDAsciiResponse(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            # ECU Serial Number = "ABC0011223344556"   (16 bytes as specified in "_Bootloader_87")
            tp_recv.return_value = [0x62, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.readDataByIdentifier('ECU Serial Number')	# ... calls __readDataByIdentifier, which does the Uds.send
    	
            tp_send.assert_called_with([0x22, 0xF1, 0x8C], False)
            self.assertEqual({'ECU Serial Number':'ABC0011223344556'}, b)
		
    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the read data by identifier (RDBI) for a single DID with a mixed response
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response with both the number of modules and Boot Software Identification DID data.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Calls the 'readDataByIdentifier' method on the Uds connection object with the DID 'Boot Software Identification'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x80] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'readDataByIdentifier' is a dictionary with the correct keys and values:
    #    - 'Boot Software Identification' with the expected ASCII value "SwId12345678901234567890".
    #    - 'numberOfModules' with the expected value [0x01].
    def test_rdbiSingleDIDMixedResponse(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            # numberOfModules = 0x01   (1 bytes as specified in "_Bootloader_1")
            # Boot Software Identification = "SwId12345678901234567890"   (24 bytes as specified in "_Bootloader_71")
            tp_recv.return_value = [0x62, 0xF1, 0x80, 0x01, 0x53, 0x77, 0x49, 0x64, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30]
    
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.readDataByIdentifier('Boot Software Identification')	# ... calls __readDataByIdentifier, which does the Uds.send
    
            tp_send.assert_called_with([0x22, 0xF1, 0x80], False)
            self.assertEqual({'Boot Software Identification': 'SwId12345678901234567890','numberOfModules': [0x01]}, b)

		
    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the read data by identifier (RDBI) for multiple DIDs with a mixed response
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response with both ECU Serial Number and Boot Software Identification DID data.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Calls the 'readDataByIdentifier' method on the Uds connection object with the DIDs 'ECU Serial Number' and 'Boot Software Identification'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C, 0xF1, 0x80] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'readDataByIdentifier' is a tuple containing two dictionaries:
    #    - The first dictionary contains 'ECU Serial Number' with the expected ASCII value "ABC0011223344556".
    #    - The second dictionary contains:
    #      - 'Boot Software Identification' with the expected ASCII value "SwId12345678901234567890".
    #      - 'numberOfModules' with the expected value [0x01].
    def test_rdbiMultipleDIDMixedResponse(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x62, 0xF1, 0x8C, 0xF1, 0x80]
            # ECU Serial Number = "ABC0011223344556"   (16 bytes as specified in "_Bootloader_87")
            # numberOfModules = 0x01   (1 bytes as specified in "_Bootloader_1")
            # Boot Software Identification = "SwId12345678901234567890"   (24 bytes as specified in "_Bootloader_71")
            tp_recv.return_value = [0x62, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36, 0xF1, 0x80, 0x01, 0x53, 0x77, 0x49, 0x64, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30]
    
    
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.readDataByIdentifier(['ECU Serial Number','Boot Software Identification'])	# ... calls __readDataByIdentifier, which does the Uds.send
    	
            tp_send.assert_called_with([0x22, 0xF1, 0x8C, 0xF1, 0x80], False)
            self.assertEqual(({'ECU Serial Number':'ABC0011223344556'},{'Boot Software Identification':'SwId12345678901234567890','numberOfModules':[0x01]}), b)


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the read data by identifier (RDBI) for multiple DIDs with alternative ordering
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response with both Boot Software Identification and ECU Serial Number DID data in an alternative order.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Calls the 'readDataByIdentifier' method on the Uds connection object with the DIDs 'Boot Software Identification' and 'ECU Serial Number'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x80, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'readDataByIdentifier' is a tuple containing two dictionaries:
    #    - The first dictionary contains:
    #      - 'Boot Software Identification' with the expected ASCII value "SwId12345678901234567890".
    #      - 'numberOfModules' with the expected value [0x01].
    #    - The second dictionary contains 'ECU Serial Number' with the expected ASCII value "ABC0011223344556".
    
    def test_rdbiMultipleDIDAlternativeOrdering(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x62, 0xF1, 0x80, 0xF1, 0x8C]
            # numberOfModules = 0x01   (1 bytes as specified in "_Bootloader_1")
            # Boot Software Identification = "SwId12345678901234567890"   (24 bytes as specified in "_Bootloader_71")
            # ECU Serial Number = "ABC0011223344556"   (16 bytes as specified in "_Bootloader_87")
            tp_recv.return_value = [0x62, 0xF1, 0x80, 0x01, 0x53, 0x77, 0x49, 0x64, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.readDataByIdentifier(['Boot Software Identification','ECU Serial Number'])	# ... calls __readDataByIdentifier, which does the Uds.send
    	
            tp_send.assert_called_with([0x22, 0xF1, 0x80, 0xF1, 0x8C], False)
            self.assertEqual(({'Boot Software Identification':'SwId12345678901234567890','numberOfModules':[0x01]},{'ECU Serial Number':'ABC0011223344556'}), b)


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the ECU Reset service
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Attempts to call the 'readDataByIdentifier' method on the Uds connection object with the DID 'ECU Serial Number'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    
    def test_ecuResetNegResponse_0x13(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.readDataByIdentifier('ECU Serial Number')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x22, 0xF1, 0x8C], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... rdbi should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the ECU Reset service
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Attempts to call the 'readDataByIdentifier' method on the Uds connection object with the DID 'ECU Serial Number'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    
    def test_ecuResetNegResponse_0x22(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.readDataByIdentifier('ECU Serial Number')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x22, 0xF1, 0x8C], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)  # ... rdbi should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the ECU Reset service
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Attempts to call the 'readDataByIdentifier' method on the Uds connection object with the DID 'ECU Serial Number'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    
    def test_ecuResetNegResponse_0x31(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.readDataByIdentifier('ECU Serial Number')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x22, 0xF1, 0x8C], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)  # ... rdbi should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x33) for the ECU Reset service
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x33.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    #    - This initializes the Uds instance and parses the read data by identifier (RDBI) information from the ODX file.
    # 4. Attempts to call the 'readDataByIdentifier' method on the Uds connection object with the DID 'ECU Serial Number'.
    #    - This method internally calls the '__readDataByIdentifier' method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x22, 0xF1, 0x8C] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x33']".
    
    def test_ecuResetNegResponse_0x33(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x33]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.readDataByIdentifier('ECU Serial Number')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x22, 0xF1, 0x8C], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x33']", b)  # ... rdbi should not return a value



if __name__ == "__main__":
    unittest.main()
