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
from uds.uds_config_tool.ISOStandard.ISOStandard import IsoRoutineControlType

class ECUResetTestCase(unittest.TestCase):

    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    <<function_definition:0>> 


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    <<function_definition:1>> 

		
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request with suppressPosRspMsgIndicationBit set to True
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 3. Calls the 'routineControl' method on the Uds connection object with the specified routine, control type, parameters, and suppressResponse flag set to True.
    # 4. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x81, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 5. Asserts that the return value from 'routineControl' is None, indicating that no value is expected to be returned when the response is suppressed.
    
    def test_routineControlRequestSuppress(self,
                         canTp_send):
    
            canTp_send.return_value = False
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])], suppressResponse=True)	# ... calls __routineControl, which does the Uds.send
    	
            canTp_send.assert_called_with([0x31, 0x81, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual(None, b)  # ... routineControl should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    <<function_definition:3>> 


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    <<function_definition:4>> 


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request for checking valid application start
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the routine control request to check valid application start.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Calls the 'routineControl' method on the Uds connection object with the specified routine and control type set to startRoutine.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'routineControl' is a dictionary containing:
    #    - 'Valid Application Status' with the expected value [0x30].
    #    - 'Valid Application Present' with the expected value [0x02].
    #    - 'RoutineControlType' with the expected value [0x01].
    #    - 'Identifier' with the expected value [0x03, 0x04].
    
    def test_routineControlRequestCheckAppStart(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x71, 0x01, 0x03, 0x04, 0x30, 0x02]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Check Valid Application', IsoRoutineControlType.startRoutine)	# ... calls __routineControl, which does the Uds.send
            canTp_send.assert_called_with([0x31, 0x01, 0x03, 0x04], False)
            self.assertEqual({'Valid Application Status':[0x30],'Valid Application Present':[0x02],'RoutineControlType':[0x01],'Identifier':[0x03, 0x04]}, b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request for checking valid application and requesting results
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the routine control request to check valid application results.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Calls the 'routineControl' method on the Uds connection object with the specified routine and control type set to requestRoutineResults.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x03, followed by the routine identifier] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'routineControl' is a dictionary containing:
    #    - 'Valid Application Status' with the expected value [0x30].
    #    - 'Valid Application Present' with the expected value [0x02].
    #    - 'RoutineControlType' with the expected value [0x03].
    #    - 'Identifier' with the expected value [0x03, 0x04].
    
    def test_routineControlRequestCheckAppStartResult(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x71, 0x03, 0x03, 0x04, 0x30, 0x02]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Check Valid Application', IsoRoutineControlType.requestRoutineResults)	# ... calls __routineControl, which does the Uds.send
    	
            canTp_send.assert_called_with([0x31, 0x03, 0x03, 0x04], False)
            self.assertEqual({'Valid Application Status':[0x30],'Valid Application Present':[0x02],'RoutineControlType':[0x03],'Identifier':[0x03, 0x04]}, b)

	
	
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request for starting the secondary bootloader (SBL)
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the routine control request to start the secondary bootloader.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Calls the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'routineControl' is a dictionary containing:
    #    - 'strSBLRoutineInfo' with the expected value [0xA7].
    #    - 'RoutineControlType' with the expected value [0x01].
    #    - 'Identifier' with the expected value [0x03, 0x01].
    
    def test_routineControlRequestSBLStart(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x71, 0x01, 0x03, 0x01, 0xA7]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Start Secondary Bootloader', IsoRoutineControlType.startRoutine, [0xFF])	# ... calls __routineControl, which does the Uds.send
            canTp_send.assert_called_with([0x31, 0x01, 0x03, 0x01, 0x00, 0x00, 0x00, 0xFF], False)
            self.assertEqual({'strSBLRoutineInfo':[0xA7],'RoutineControlType':[0x01],'Identifier':[0x03, 0x01]}, b)



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request for checking programming dependencies
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the routine control request to check programming dependencies.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Calls the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'routineControl' is a dictionary containing:
    #    - 'RoutineStatusInfo' with the expected value [0x30].
    #    - 'Check Sum Value' with the expected value [0xB9, 0x2E].
    #    - 'RoutineControlType' with the expected value [0x01].
    #    - 'Identifier' with the expected value [0xFF, 0x01].
    
    def test_routineControlRequestProgDepStart(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x71, 0x01, 0xFF, 0x01, 0x30, 0xB9, 0x2E]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Check Programming Dependencies', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual({'RoutineStatusInfo':[0x30],'Check Sum Value':[0xB9, 0x2E],'RoutineControlType':[0x01],'Identifier':[0xFF, 0x01]}, b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the routine control request for requesting programming dependencies results
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the routine control request to request programming dependencies results.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Calls the 'routineControl' method on the Uds connection object with the specified routine and control type set to requestRoutineResults.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x03, followed by the routine identifier] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'routineControl' is a dictionary containing:
    #    - 'RoutineStatusInfo' with the expected value [0x30].
    #    - 'Check Sum Value' with the expected value [0xB9, 0x2E].
    #    - 'RoutineControlType' with the expected value [0x03].
    #    - 'Identifier' with the expected value [0xFF, 0x01].
    
    def test_routineControlRequestProgDepResult(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x71, 0x03, 0xFF, 0x01, 0x30, 0xB9, 0x2E]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            b = a.routineControl('Check Programming Dependencies', IsoRoutineControlType.requestRoutineResults)	# ... calls __routineControl, which does the Uds.send
            canTp_send.assert_called_with([0x31, 0x03, 0xFF, 0x01], False)
            self.assertEqual({'RoutineStatusInfo':[0x30],'Check Sum Value':[0xB9, 0x2E],'RoutineControlType':[0x03],'Identifier':[0xFF, 0x01]}, b)



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x12) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x12.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x12']".
    
    def test_ecuResetNegResponse_0x12(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x12]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x12']", b)

    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    
    def test_ecuResetNegResponse_0x13(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x22) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x22.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x22']".
    
    def test_ecuResetNegResponse_0x22(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x22]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x22']", b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x24) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x24.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x24']".
    
    def test_ecuResetNegResponse_0x24(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x24]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x24']", b)



    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    
    def test_ecuResetNegResponse_0x31(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x33) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x33.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x33']".
    
    def test_ecuResetNegResponse_0x33(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x33]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x33']", b)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x72) for the routine control request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x72.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __routineControl method to routineControl in the Uds object.
    # 4. Attempts to call the 'routineControl' method on the Uds connection object with the specified routine, control type set to startRoutine, and parameters.
    #    - This method internally calls the __routineControl method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message [0x31, 0x01, followed by the routine identifier and parameters] and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x72']".
    
    def test_ecuResetNegResponse_0x72(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x72]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __routineControl to routineControl in the uds object, so can now call below
    
            try:
                b = a.routineControl('Erase Memory', IsoRoutineControlType.startRoutine, [('memoryAddress', [0x01]),('memorySize', [0xF000])])	# ... calls __routineControl, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x31, 0x01, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xF0, 0x00], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x72']", b)





if __name__ == "__main__":
    unittest.main()