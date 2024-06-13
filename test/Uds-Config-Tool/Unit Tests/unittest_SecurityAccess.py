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
    # Test method to verify the security access key request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a successful security access seed response.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    # 4. Calls the 'securityAccess' method on the Uds connection object with the security level 'Programming Request'.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x27, 0x01] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'securityAccess' is a list of 16 bytes with all values set to 0x00, representing the expected seed.
    def test_securityAccessKeyRequest(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x67, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
    
            b = a.securityAccess('Programming Request')
    
            tp_send.assert_called_with([0x27, 0x01], False)
            self.assertEqual([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                             b)  # ... securityAccess should return the seed value

    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the handling of a negative response for the security access request
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a negative response with service identifier 0x7F and code 0x00.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    # 4. Calls the 'securityAccess' method on the Uds connection object with the security level 'Programming Request' and expects it to raise an exception.
    #    - Uses 'assertRaises' to check that an exception is raised.
    # 5. Asserts that the exception message contains the string "Found negative response", indicating that a negative response was correctly identified and handled.
    def test_securityAccessNegativeResponse(self,
                                  tp_send,
                                  tp_recv):
            tp_send.return_value = False
            tp_recv.return_value = [0x7F, 0x00, 0x00]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx',
                                    'bootloader',
                                    transportProtocol="TEST")
    
            with self.assertRaises(Exception) as context:
                b = a.securityAccess('Programming Request')
    
            self.assertTrue("Found negative response" in str(context.exception))

    # patches are inserted in reverse order
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify the security access key submission
    # Args:
    #    self: The instance of the test case class.
    #    tp_send: A mock object for the transport protocol's send method.
    #    tp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a list representing a successful security access key response.
    # 3. Creates a Uds connection using the provided XML file (ODX file) and transport protocol "TEST".
    # 4. Calls the 'securityAccess' method on the Uds connection object with the security level 'Programming Key' and the provided key.
    # 5. Asserts that the 'tp_send' mock was called with the expected message [0x27, 0x02, followed by the key] and the responseRequired flag set to False.
    # 6. Asserts that the return value from 'securityAccess' is None, indicating that no value is expected to be returned after submitting the key.
    
    def test_securityAccessKeyRequest(self,
                         tp_send,
                         tp_recv):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x67, 0x02]
    
            # Parameters: xml file (odx file), ecu name (not currently used), transport protocol ...
            a = createUdsConnection('../Functional Tests/Bootloader.odx',
                                    'bootloader',
                                    transportProtocol="TEST")
    
            b = a.securityAccess('Programming Key',
                                 [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    
            tp_send.assert_called_with([0x27, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                        0x00, 0x00],
                                       False)
            self.assertEqual(None, b)  # ... securityAccess should not return a value after key submission



if __name__ == "__main__":
    unittest.main()
