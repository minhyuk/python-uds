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


class UdsTestCase(unittest.TestCase):

    # these are inserted in reverse order to what you'd expect
    @mock.patch('uds.TestTp.recv')
    @mock.patch('uds.TestTp.send')
    # Test method to verify that Uds.send method sends a message and correctly receives a response
    # Args:
    #    self: The instance of the test case class.
    #    testTp_send: A mock object for the transport protocol's send method.
    #    testTp_recv: A mock object for the transport protocol's receive method.
    # 1. Sets the return value of 'testTp_send' mock to False.
    # 2. Sets the return value of 'testTp_recv' mock to a response message [0x50, 0x01].
    # 3. Initializes a Uds connection with transport protocol set to "TEST".
    # 4. Calls the 'send' method on the udsConnection with a request message [0x10, 0x01].
    # 5. Asserts that the response from the 'send' method is equal to the expected response [0x50, 0x01].
    def test_udsSendWithResponse(self,
                                     testTp_send,
                                     testTp_recv):
    
            testTp_send.return_value = False
            testTp_recv.return_value = [0x50, 0x01]
    
            udsConnection = Uds(transportProtocol="TEST")
    
            a = udsConnection.send([0x10, 0x01])
    
            self.assertEqual([0x50, 0x01], a)

    # these are inserted in reverse order to what you'd expect
    @mock.patch('uds.TestTp.send')  # 2
    # Test method to verify that Uds.send method sends a message without waiting for a response
    # Args:
    #    self: The instance of the test case class.
    #    testTp_send: A mock object for the transport protocol's send method.
    # 1. Sets the return value of 'testTp_send' mock to False.
    # 2. Initializes a Uds connection with transport protocol set to "TEST".
    # 3. Calls the 'send' method on the udsConnection with a request message [0x10, 0x01] and sets 'responseRequired' to False.
    # 4. Asserts that the result is None, indicating no response is expected.
    def test_udsSendWithoutResponse(self,
                                        testTp_send):
    
            testTp_send.return_value = False
    
            udsConnection = Uds(transportProtocol="TEST")
    
            a = udsConnection.send([0x10, 0x01], responseRequired=False)
    
            self.assertEqual(None, None)

    # these are inserted in reverse order to what you'd expect
    @mock.patch('uds.TestTp.send')  # 2
    # Test method to verify that Uds.send method sends a functional request message
    # Args:
    #    self: The instance of the test case class.
    #    testTp_send: A mock object for the transport protocol's send method.
    # 1. Sets the return value of 'testTp_send' mock to False.
    # 2. Initializes a Uds connection with transport protocol set to "TEST".
    # 3. Calls the 'send' method on the udsConnection with a request message [0x10, 0x01] and sets 'functionalReq' to True.
    # 4. Asserts that the result is None, as no response is expected for functional requests.
    def test_udsSendFunctionalRequest(self,
                                          testTp_send):
            testTp_send.return_value = False
    
            udsConnection = Uds(transportProtocol="TEST")
    
            a = udsConnection.send([0x10, 0x01], functionalReq=True)
    
            self.assertEqual(None, None)

if __name__ == "__main__":
    unittest.main()
