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
from uds.uds_config_tool.ISOStandard.ISOStandard import IsoInputOutputControlOptionRecord as IsoOptionRecord
import sys, traceback


class IOControlTestCase(unittest.TestCase):

    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the input/output control service (adjust) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response for the input/output control request (adjust).
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Calls the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.adjust', and target speed value [8000].
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'inputOutputControl' is a dictionary containing:
    #    - 'Identifier' with the expected values [0xFE, 0x16].
    #    - 'ControlOptionRecord' with the expected value 'IsoOptionRecord.adjust'.
    #    - 'TargetSpeed' with the expected values [0x00, 0x00, 0x1F, 0x40].
    
    def test_ioControlRequest_adjust(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False	
            tp_recv.return_value = [0x6F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.adjust, [8000])  # ... calls __inputOutputControl, which does the Uds.send
    
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40], False)
            self.assertEqual({'Identifier':[0xFE, 0x16],'ControlOptionRecord':[IsoOptionRecord.adjust],'TargetSpeed':[0x00, 0x00, 0x1F, 0x40]}, b)


    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the input/output control service (return control) request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a valid response for the input/output control request (return control).
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Calls the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.returnControl', and no additional parameters (None).
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x00] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'inputOutputControl' is a dictionary containing:
    #    - 'Identifier' with the expected values [0xFE, 0x16].
    #    - 'ControlOptionRecord' with the expected value 'IsoOptionRecord.returnControl'.
    #    - 'TargetSpeed' with the expected values [0x00, 0x00, 0x1F, 0x40].
    
    def test_ioControlRequest_returnControl(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False	
            tp_recv.return_value = [0x6F, 0xFE, 0x16, 0x00, 0x00, 0x00, 0x1F, 0x40]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.returnControl, None)	# ... calls __inputOutputControl, which does the Uds.send
    
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x00], False)
            self.assertEqual({'Identifier':[0xFE, 0x16],'ControlOptionRecord':[IsoOptionRecord.returnControl],'TargetSpeed':[0x00, 0x00, 0x1F, 0x40]}, b)
		

    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the input/output control request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Attempts to call the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.adjust', and target speed value [8000].
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    
    def test_ecuResetNegResponse_0x13(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            try:
                b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.adjust, [8000])	# ... calls __inputOutputControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)



    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the input/output control request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Attempts to call the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.adjust', and target speed value [8000].
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    
    def test_ecuResetNegResponse_0x22(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            try:
                b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.adjust, [8000])	# ... calls __inputOutputControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)



    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the input/output control request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Attempts to call the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.adjust', and target speed value [8000].
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    
    def test_ecuResetNegResponse_0x31(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            try:
                b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.adjust, [8000])	# ... calls __inputOutputControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)



    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x33) for the input/output control request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x33.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader', along with transport protocol "TEST".
    #    - This initializes the Uds instance and attaches the __inputOutputControl method to inputOutputControl in the Uds object.
    # 4. Attempts to call the 'inputOutputControl' method on the Uds connection object with the control name 'Booster Target Speed', control option record set to 'IsoOptionRecord.adjust', and target speed value [8000].
    #    - This method internally calls the __inputOutputControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'tp_send' mock was called with the expected message [0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x33']".
    
    def test_ecuResetNegResponse_0x33(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x33]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/EBC-Diagnostics_old.odx', 'bootloader', transportProtocol="TEST")
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __inputOutputControl to inputOutputControl in the uds object, so can now call below
    
            try:
                b = a.inputOutputControl('Booster Target Speed', IsoOptionRecord.adjust, [8000])	# ... calls __inputOutputControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            tp_send.assert_called_with([0x2F, 0xFE, 0x16, 0x03, 0x00, 0x00, 0x1F, 0x40], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x33']", b)

	



if __name__ == "__main__":
    unittest.main()