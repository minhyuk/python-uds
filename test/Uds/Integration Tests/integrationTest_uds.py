"""
The script defines a test case class UdsTestCase for testing the behavior and functionality of the Uds class, specifically focusing on the send
method with response. The test case class inherits from unittest.TestCase and includes a single test method named test_udsSendWithResponse.

The test_udsSendWithResponse method utilizes mocking with patch decorators to simulate the behaviors of the send and receive functions of the TestTp
class, enabling controlled responses for testing purposes. The method sets up the expected return values for the mocked functions to simulate a send
operation and a subsequent response.

Inside the test method:
- The send method of the Uds class is called with a specific payload ([0x10, 0x01]).
- The mocked send function returns False, indicating a failed send operation.
- The mocked receive function returns a specific response data ([0x50, 0x01]) that is expected to be received after the send operation.
- The actual response data obtained from the Uds send method is stored in variable 'a'.

The test method then asserts that the received response 'a' matches the expected data ([0x50, 0x01]), ensuring that the Uds class behaves correctly
by sending data and processing the response accordingly.

The script concludes with unittest.main() that executes the test case by running the defined test methods in the UdsTestCase class.
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
from uds import Uds
from unittest import mock

class UdsTestCase(unittest.TestCase):

    # Define test method for Uds class send operation with response
    @mock.patch('uds.TestTp.send')
    @mock.patch('uds.TestTp.recv')
    def test_udsSendWithResponse(self, tp_recv, tp_send):
        ...
        
if __name__ == "__main__":
    # Execute the test methods in the UdsTestCase class
    unittest.main()
"""
