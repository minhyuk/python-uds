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


class WDBITestCase(unittest.TestCase):
	
    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the write data by identifier (WDBI) request for an ASCII value
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a successful WDBI response with identifier 0xF1 0x8C.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Calls the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, followed by the ASCII characters 'ABC0011223344556'] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'writeDataByIdentifier' is None, indicating that no value is expected to be returned for the WDBI request.
    
    def test_wdbiAsciiRequest(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x6E, 0xF1, 0x8C]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
    
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual(None, b)  # ... WDBI should not return a value
		
		

    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the write data by identifier (WDBI) request for mixed data types
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a successful WDBI response with identifier 0xF1 0x80.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Calls the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'Boot Software Identification' and a list of tuples representing mixed data types:
    #    - ('Boot Software Identification', 'SwId12345678901234567890')
    #    - ('numberOfModules', [0x01])
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x80, 0x00, 0x00, 0x00, 0x01, followed by 'SwId12345678901234567890'] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'writeDataByIdentifier' is None, indicating that no value is expected to be returned for the WDBI request.
    
    def test_wdbiMixedRequest(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x6E, 0xF1, 0x80]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.writeDataByIdentifier('Boot Software Identification', [('Boot Software Identification', 'SwId12345678901234567890'), ('numberOfModules', [0x01])])	# ... calls __readDataByIdentifier, which does the Uds.send
    
            tp_send.assert_called_with([0x2E, 0xF1, 0x80, 0x00, 0x00, 0x00, 0x01, 0x53, 0x77, 0x49, 0x64, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30], False)
            self.assertEqual(None, b)  # ... WDBI should not return a value

		

    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the write data by identifier (WDBI) request for mixed data types in reverse order
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a successful WDBI response with identifier 0xF1 0x80.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Calls the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'Boot Software Identification' and a list of tuples representing mixed data types in reverse order:
    #    - ('numberOfModules', [0x01])
    #    - ('Boot Software Identification', 'SwId12345678901234567890')
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x80, 0x00, 0x00, 0x00, 0x01, followed by 'SwId12345678901234567890'] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'writeDataByIdentifier' is None, indicating that no value is expected to be returned for the WDBI request.
    
    def test_wdbiMixedRequestReverseOrder(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x6E, 0xF1, 0x80]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            b = a.writeDataByIdentifier('Boot Software Identification', [('numberOfModules', [0x01]), ('Boot Software Identification', 'SwId12345678901234567890')])	# ... calls __readDataByIdentifier, which does the Uds.send
    
            tp_send.assert_called_with([0x2E, 0xF1, 0x80, 0x00, 0x00, 0x00, 0x01, 0x53, 0x77, 0x49, 0x64, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30], False)
            self.assertEqual(None, b)  # ... WDBI should not return a value



    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the write data by identifier (WDBI) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Attempts to call the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    #    - Indicates that writeDataByIdentifier should not return a value when a negative response is detected.
    
    def test_wdbiNegResponse_0x13(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... WDBI should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the write data by identifier (WDBI) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Attempts to call the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    #    - Indicates that writeDataByIdentifier should not return a value when a negative response is detected.
    
    def test_wdbiNegResponse_0x22(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)  # ... WDBI should not return a value



    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the write data by identifier (WDBI) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Attempts to call the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    #    - Indicates that writeDataByIdentifier should not return a value when a negative response is detected.
    
    def test_wdbiNegResponse_0x31(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)  # ... WDBI should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x33) for the write data by identifier (WDBI) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x33.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Attempts to call the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x33']".
    #    - Indicates that writeDataByIdentifier should not return a value when a negative response is detected.
    
    def test_wdbiNegResponse_0x33(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x33]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x33']", b)  # ... WDBI should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x72) for the write data by identifier (WDBI) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x72.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __readDataByIdentifier method to readDataByIdentifier in the Uds object.
    # 4. Attempts to call the 'writeDataByIdentifier' method on the Uds connection object with the identifier 'ECU Serial Number' and the ASCII value 'ABC0011223344556'.
    #    - This method internally calls the __readDataByIdentifier method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x72']".
    #    - Indicates that writeDataByIdentifier should not return a value when a negative response is detected.
    
    def test_wdbiNegResponse_0x72(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x72]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __readDataByIdentifier to readDataByIdentifier in the uds object, so can now call below
    
            try:
                b = a.writeDataByIdentifier('ECU Serial Number', 'ABC0011223344556')	# ... calls __readDataByIdentifier, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2E, 0xF1, 0x8C, 0x41, 0x42, 0x43, 0x30, 0x30, 0x31, 0x31, 0x32, 0x32, 0x33, 0x33, 0x34, 0x34, 0x35, 0x35, 0x36], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x72']", b)  # ... WDBI should not return a value


if __name__ == "__main__":
    unittest.main()
