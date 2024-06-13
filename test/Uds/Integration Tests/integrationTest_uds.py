#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import unittest
from uds import Uds
from unittest import mock


class UdsTestCase(unittest.TestCase):

    # these are inserted in reverse order to what you'd expect
    @mock.patch('uds.TestTp.send')
    @mock.patch('uds.TestTp.recv')
    # Test method to verify that Uds.send method sends a message and correctly receives a response
    # Args:
    #    self: The instance of the test case class.
    #    tp_recv: A mock object for the transport protocol's receive method.
    #    tp_send: A mock object for the transport protocol's send method.
    # 1. Sets the return value of 'tp_send' mock to False, simulating a successful send operation.
    # 2. Sets the return value of 'tp_recv' mock to a response message [0x50, 0x01].
    # 3. Initializes a Uds connection.
    # 4. Calls the 'send' method on the udsConnection with a request message [0x10, 0x01].
    # 5. Asserts that the response from the 'send' method is equal to the expected response [0x50, 0x01].
    def test_udsSendWithResponse(self,
                         tp_recv,
                         tp_send):
    
            tp_send.return_value = False
            tp_recv.return_value = [0x50, 0x01]
    
            udsConnection = Uds()
    
            a = udsConnection.send([0x10, 0x01])
    
            self.assertEqual([0x50, 0x01], a)


if __name__ == "__main__":
    unittest.main()
