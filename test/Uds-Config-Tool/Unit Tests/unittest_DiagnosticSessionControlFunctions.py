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


class DiagnosticSessionControlTestCase(unittest.TestCase):

    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the diagnostic session control request with default parameters and no suppressPosRspMsgIndicationBit set to True
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the diagnostic session control request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Calls the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session'.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x01] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'diagnosticSessionControl' is a dictionary containing:
    #    - 'Type' with the expected value [0x01].
    #    - 'P3' with the expected values [0x00, 0x05].
    #    - 'P3Ex' with the expected values [0x00, 0x0A].
    
    def test_diagSessCtrlRequestDfltNoSuppress(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x50, 0x01, 0x00, 0x05, 0x00, 0x0A] # ... can return 1 to N bytes in the sessionParameterRecord - looking into this one
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            b = a.diagnosticSessionControl('Default Session')	# ... calls __diagnosticSessionControl, which does the Uds.send
            canTp_send.assert_called_with([0x10, 0x01], False)
            self.assertEqual({'Type':[0x01], 'P3':[0x00, 0x05], 'P3Ex':[0x00, 0x0A]}, b)  # ... diagnosticSessionControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the diagnostic session control request with suppressPosRspMsgIndicationBit set to False
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the diagnostic session control request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Calls the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session' and suppressResponse flag set to False.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x01] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'diagnosticSessionControl' is a dictionary containing:
    #    - 'Type' with the expected value [0x01].
    #    - 'P3' with the expected values [0x00, 0x05].
    #    - 'P3Ex' with the expected values [0x00, 0x0A].
    
    def test_diagSessCtrlRequestNoSuppress(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x50, 0x01, 0x00, 0x05, 0x00, 0x0A] # ... can return 1 to N bytes in the sessionParameterRecord - looking into this one
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            b = a.diagnosticSessionControl('Default Session', suppressResponse=False)	# ... calls __diagnosticSessionControl, which does the Uds.send
            canTp_send.assert_called_with([0x10, 0x01], False)
            self.assertEqual({'Type':[0x01], 'P3':[0x00, 0x05], 'P3Ex':[0x00, 0x0A]}, b)  # ... diagnosticSessionControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.send')
    # Test method to verify the diagnostic session control request with suppressPosRspMsgIndicationBit set to True
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 3. Calls the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session' and suppressResponse flag set to True.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 4. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x81] and the responseRequired flag set to False.
    # 5. Asserts that the return value from 'diagnosticSessionControl' is None, indicating that no value is expected to be returned when the response is suppressed.
    
    def test_diagSessCtrlRequestSuppress(self,
                         canTp_send):
    
            canTp_send.return_value = False
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            b = a.diagnosticSessionControl('Default Session', suppressResponse=True)	# ... calls __diagnosticSessionControl, which does the Uds.send
            canTp_send.assert_called_with([0x10, 0x81], False)
            self.assertEqual(None, b)  # ... diagnosticSessionControl should not return a value




    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the diagnostic session control request for the 'Programming Session'
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the diagnostic session control request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Calls the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Programming Session'.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x02] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'diagnosticSessionControl' is a dictionary containing:
    #    - 'Type' with the expected value [0x02].
    #    - 'P3' with the expected values [0x00, 0x06].
    #    - 'P3Ex' with the expected values [0x00, 0x09].
    
    def test_diagSessCtrlRequestProgrammingSession(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x50, 0x02, 0x00, 0x06, 0x00, 0x09] # ... can return 1 to N bytes in the sessionParameterRecord - looking into this one
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            b = a.diagnosticSessionControl('Programming Session')	# ... calls __diagnosticSessionControl, which does the Uds.send
            canTp_send.assert_called_with([0x10, 0x02], False)
            self.assertEqual({'Type':[0x02], 'P3':[0x00, 0x06], 'P3Ex':[0x00, 0x09]}, b)  # ... diagnosticSessionControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the diagnostic session control request for the 'Extended Diagnostic Session'
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the diagnostic session control request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Calls the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Extended Diagnostic Session'.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x03] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'diagnosticSessionControl' is a dictionary containing:
    #    - 'Type' with the expected value [0x03].
    #    - 'P3' with the expected values [0x00, 0x07].
    #    - 'P3Ex' with the expected values [0x00, 0x08].
    
    def test_diagSessCtrlRequestExtendedDiagnosticSession(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x50, 0x03, 0x00, 0x07, 0x00, 0x08] # ... can return 1 to N bytes in the sessionParameterRecord - looking into this one
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            b = a.diagnosticSessionControl('Extended Diagnostic Session')	# ... calls __diagnosticSessionControl, which does the Uds.send
            canTp_send.assert_called_with([0x10, 0x03], False)
            self.assertEqual({'Type':[0x03], 'P3':[0x00, 0x07], 'P3Ex':[0x00, 0x08]}, b)  # ... diagnosticSessionControl should not return a value



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x12) for the diagnostic session control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x12.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Attempts to call the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session' and suppressResponse flag set to False.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x01] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x12']".
    #    - Indicates that diagnosticSessionControl should not return a value when a negative response is detected.
    
    def test_diagSessCtrlNegResponse_0x12(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x12]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            try:
                b = a.diagnosticSessionControl('Default Session', suppressResponse=False)	# ... calls __diagnosticSessionControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x10, 0x01], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x12']", b)  # ... diagnosticSessionControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the diagnostic session control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Attempts to call the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session' and suppressResponse flag set to False.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x01] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    #    - Indicates that diagnosticSessionControl should not return a value when a negative response is detected.
    
    def test_diagSessCtrlNegResponse_0x13(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            try:
                b = a.diagnosticSessionControl('Default Session', suppressResponse=False)	# ... calls __diagnosticSessionControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x10, 0x01], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... diagnosticSessionControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the diagnostic session control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __diagnosticSessionControl method to diagnosticSessionControl in the Uds object.
    # 4. Attempts to call the 'diagnosticSessionControl' method on the Uds connection object with the session type 'Default Session' and suppressResponse flag set to False.
    #    - This method internally calls the __diagnosticSessionControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x10, 0x01] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    #    - Indicates that diagnosticSessionControl should not return a value when a negative response is detected.
    
    def test_diagSessCtrlNegResponse_0x22(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __diagnosticSessionControl to diagnosticSessionControl in the uds object, so can now call below
    
            try:
                b = a.diagnosticSessionControl('Default Session', suppressResponse=False)	# ... calls __diagnosticSessionControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x10, 0x01], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)  # ... diagnosticSessionControl should not return a value




if __name__ == "__main__":
    unittest.main()