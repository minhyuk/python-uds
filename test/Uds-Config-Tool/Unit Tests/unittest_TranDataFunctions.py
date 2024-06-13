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
from uds.uds_config_tool.IHexFunctions import ihexFile
import sys, traceback


class TransferDataTestCase(unittest.TestCase):

    """ Note: this has been run with a modified Uds.py transferIHexFile() function to skip the reqDownload and transExit (I couldn't figure out how to mock these here)  
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    def test_transDataRequest_ihex(self,
                     canTp_send,
                     canTp_recv,
                     reqDownload,
                     transExit):

        canTp_send.return_value = False
        canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]

        # Parameters: xml file (odx file), ecu name (not currently used) ...
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
        # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below

        b = a.transferFile("./unitTest01.hex",1280)	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
	
        canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53],False)
        self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)
    """
		

    """ REMOVING THIS TEST AS "block" list is no longer exposed this way ...
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    def test_transDataRequest_ihex01(self,
                     canTp_send,
                     canTp_recv):

        canTp_send.return_value = False
        canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]

        app_blocks = ihexFile("./unitTest01.hex")
        app_blocks.transmitChunksize = 1280

        # Parameters: xml file (odx file), ecu name (not currently used) ...
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
        # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below

        b = a.transferData(transferBlock=app_blocks.block[0])	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
	
        canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53],False)
        self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)
    """


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer data request when using an Intel HEX file
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer data request.
    # 3. Initializes 'app_blocks' by reading data from an Intel HEX file and sets the transmit chunk size to 1280 bytes.
    # 4. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 5. Calls the 'transferData' method on the Uds connection object with the specified transfer blocks.
    #    - This method internally calls the __transferData method using the Uds.send method, taking the blockSequenceCounter and parameterRecord.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the required bytes, and the responseRequired flag set to False.
    # 7. Asserts that the return value from 'transferData' is a dictionary containing:
    #    - 'blockSequenceCounter' with the expected value [0x01].
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transDataRequest_ihex02(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            app_blocks = ihexFile("./unitTest01.hex")
            app_blocks.transmitChunksize = 1280
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            b = a.transferData(transferBlocks=app_blocks)	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
    	
            canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53], False)
            self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)


    """ REMOVING THIS TEST AS "block" list is no longer exposed this way ...
    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    def test_transDataRequest_ihex03(self,
                     canTp_send,
                     canTp_recv):

        canTp_send.return_value = False
        canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]

        # Parameters: xml file (odx file), ecu name (not currently used) ...
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader',ihexFile="./unitTest01.hex")
        a.ihexFile.transmitChunksize = 1280
        # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below

        b = a.transferData(transferBlock=a.ihexFile.block[0])	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
	
        canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53],False)
        self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)
    """


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer data request when using an Intel HEX file (specified in createUdsConnection)
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer data request.
    # 3. Creates a Uds connection using the provided XML file (ODX file), ECU name 'bootloader', and Intel HEX file path "unitTest01.hex".
    #    - This initializes the Uds instance, attaches the __transferData method to transferData in the Uds object, and sets the transmit chunk size to 1280 bytes.
    # 4. Calls the 'transferData' method on the Uds connection object with the specified transfer blocks from the Intel HEX file.
    #    - This method internally calls the __transferData method using the Uds.send method, taking the blockSequenceCounter and parameterRecord.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the required bytes, and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'transferData' is a dictionary containing:
    #    - 'blockSequenceCounter' with the expected value [0x01].
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transDataRequest_ihex04(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            # Parameters: xml file (odx file), ecu name (not currently used), Intel HEX file
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', ihexFile="./unitTest01.hex")
            a.ihexFile.transmitChunksize = 1280
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            b = a.transferData(transferBlocks=a.ihexFile)	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
    	
            canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53], False)
            self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer data request when using an Intel HEX file, with the file set after UDS creation
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer data request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - Sets the Intel HEX file path (ihexFile) after creating the Uds connection object, and sets the transmit chunk size to 1280 bytes.
    # 4. Calls the 'transferData' method on the Uds connection object with the specified transfer blocks from the Intel HEX file.
    #    - This method internally calls the __transferData method using the Uds.send method, taking the blockSequenceCounter and parameterRecord.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the required bytes, and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'transferData' is a dictionary containing:
    #    - 'blockSequenceCounter' with the expected value [0x01].
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transDataRequest_ihex05(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            a.ihexFile = "./unitTest01.hex"
            a.ihexFile.transmitChunksize = 1280
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            b = a.transferData(transferBlocks=a.ihexFile)	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
    	
            canTp_send.assert_called_with([0x36, 0x01, 0x00, 0x08, 0x00, 0x70, 0x00, 0x09, 0x4E, 0x80, 0x45, 0x34, 0x30, 0x30, 0x2D, 0x55, 0x44, 0x53], False)
            self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer data request using explicit block sequence counter and parameter record
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer data request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Calls the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'transferData' is a dictionary containing:
    #    - 'blockSequenceCounter' with the expected value [0x01].
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transDataRequest(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x76, 0x01, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
    	
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual({'blockSequenceCounter':[0x01],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a transfer data request using block sequence counter 0x02 and a specific parameter record
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a valid response for the transfer data request.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Calls the 'transferData' method on the Uds connection object with the specified block sequence counter 0x02 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x02] followed by the parameter record, and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'transferData' is a dictionary containing:
    #    - 'blockSequenceCounter' with the expected value [0x02].
    #    - 'transferResponseParameterRecord' with the expected bytes received [0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF].
    
    def test_transDataRequestSeq02(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x76, 0x02, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            b = a.transferData(0x02, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send - takes blockSequenceCounter and parameterRecord
    	
            canTp_send.assert_called_with([0x36, 0x02, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual({'blockSequenceCounter':[0x02],'transferResponseParameterRecord':[0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF]}, b)  # ... (returns a dict)




    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x13) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x13.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x13']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x13(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x13]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x13']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x24) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x24.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x24']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x24(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x24]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x24']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x31) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x31.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x31']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x31(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x31]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x31']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x71) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x71.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x71']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x71(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x71]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x71']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x72) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x72.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x72']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x72(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x72]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x72']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x73) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x73.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x73']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x73(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x73]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x73']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x92) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x92.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x92']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x92(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x92]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x92']", b)  # ... transferData should not return a value


    # patches are inserted in reverse order
    @mock.patch('uds.CanTp.recv')
    @mock.patch('uds.CanTp.send')
    # Test method to verify the handling of a negative response (0x7F, 0x93) for the transfer data request
    # Args:
    #    self: The instance of the test case class.
    #    canTp_send: A mock object for the transport protocol's send method.
    #    canTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'canTp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'canTp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x93.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and ECU name 'bootloader'.
    #    - This initializes the Uds instance and attaches the __transferData method to transferData in the Uds object.
    # 4. Attempts to call the 'transferData' method on the Uds connection object with the specified block sequence counter 0x01 and parameter record [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF].
    #    - This method internally calls the __transferData method using the Uds.send method.
    # 5. Catches the exception if a negative response is detected and extracts the exception text for verification.
    # 6. Asserts that the 'canTp_send' mock was called with the expected message beginning [0x36, 0x01] followed by the parameter record, and the responseRequired flag set to False.
    # 7. Asserts that the exception message matches the expected negative response message "Exception: Detected negative response: ['0x7f', '0x93']".
    #    - Indicates that transferData should not return a value when a negative response is detected.
    
    def test_transDataNegResponse_0x93(self,
                         canTp_send,
                         canTp_recv):
    
            canTp_send.return_value = False
            canTp_recv.return_value = [0x7F, 0x93]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader')
            # ... creates the uds object and returns it; also parses out the rdbi info and attaches the __transferData to transferData in the uds object, so can now call below
    
            try:
                b = a.transferData(0x01, [0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF])	# ... calls __transferData, which does the Uds.send
            except:
                b = traceback.format_exc().split("\n")[-2:-1][0] # ... extract the exception text
            canTp_send.assert_called_with([0x36, 0x01, 0xF1, 0xF2, 0xF3, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF], False)
            self.assertEqual("Exception: Detected negative response: ['0x7f', '0x93']", b)  # ... transferData should not return a value


if __name__ == "__main__":
    unittest.main()