"""
The script contains a series of unit test cases that validate specific scenarios for the 'securityAccess' function in the UDS protocol implementation.

Key Functionalities:

1. Import:
    - Importing the necessary modules and functions to create a UdsConnection and conduct unit testing.

2. Test Cases:
    a. test_securityAccessKeyRequest:
        - Validates the behavior of requesting a security access key.
    
    b. test_securityAccessNegativeResponse:
        - Ensures the handling of negative responses during security access request.
    
    c. test_securityAccessKeyRequest:
        - Validates the process of requesting a security access key with specific input parameters.

3. Testing Procedure:
    - Utilizes the mock.patch function to simulate interactions with the Test Transport Protocol (TestTp).
    - Verifies the expected responses and behavior based on the provided input parameters during security access operations.
    - Tests the functionality of handling negative responses and ensuring the appropriate error handling mechanism.

4. Execution:
    - Executes the defined unit test cases using the unittest module for validation.
    - Utilizes the TestTp for sending and receiving data in a simulated environment.

Overall, the script focuses on testing the functionality of security access operations within the UDS protocol implementation, covering scenarios such as key requests and handling of negative responses during security access procedures.
"""

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
    # Unit test cases for securityAccess function

    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    def test_securityAccessKeyRequest(self, tp_send, tp_recv):
        # Testing security access key request
        tp_send.return_value = False
        tp_recv.return_value = [0x67, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
        b = a.securityAccess('Programming Request')
        tp_send.assert_called_with([0x27, 0x01], False)
        self.assertEqual([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
                         b)

    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    def test_securityAccessNegativeResponse(self, tp_send, tp_recv):
        # Handling negative response during security access request
        tp_send.return_value = False
        tp_recv.return_value = [0x7F, 0x00, 0x00]
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
        with self.assertRaises(Exception) as context:
            b = a.securityAccess('Programming Request')
        self.assertTrue("Found negative response" in str(context.exception))

    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    def test_securityAccessKeyRequest(self, tp_send, tp_recv):
        # Testing security access key request with specific input parameters
        tp_send.return_value = False
        tp_recv.return_value = [0x67, 0x02]
        a = createUdsConnection('../Functional Tests/Bootloader.odx', 'bootloader', transportProtocol="TEST")
        b = a.securityAccess('Programming Key',
                             [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                              0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        tp_send.assert_called_with([0x27, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                                    0x00, 0x00],
                                   False)
        self.assertEqual(None, b)

if __name__ == "__main__":
    # Execute the unit tests
    unittest.main()
"""
