#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import unittest
from unittest.mock import patch

from uds import CanTp


class CanTpTestCase(unittest.TestCase):

    # Test method to verify that CanTp raises an exception when attempting to send a payload that is too large
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates a payload list of 4096 zeroes.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Asserts that sending the payload raises an exception.
    def test_canTpRaiseExceptionOnTooLargePayload(self):
            payload = []
            for i in range(0, 4096):
                payload.append(0)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
            with self.assertRaises(Exception):
                tpConnection.send(payload)

    @patch('can.interfaces.virtual.VirtualBus.send')
    # Test method to verify that CanTp sends a single frame correctly
    # Args:
    #    self: The instance of the test case class.
    #    sendMock: A mock object for the send method.
    # 1. Initializes an empty list 'result' to store the sent data.
    # 2. Defines a function 'msgData' to capture the message data sent by the mock and extend 'result' with message data.
    # 3. Sets the side effect of 'sendMock' to 'msgData' function to capture what is being sent.
    # 4. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 5. Defines a payload list with specific data bytes [0x01, 0x02, 0x03].
    # 6. Sends the payload using the CanTp connection.
    # 7. Asserts that 'result' matches the expected frame data after sending.
    def test_canTpSendSingleFrame(self, sendMock):
    
            result = []
    
            def msgData(msg):
                result.extend(msg.data)
    
            sendMock.side_effect = msgData
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            payload = [0x01, 0x02, 0x03]
            tpConnection.send(payload)
    
            self.assertEqual(result, [0x03, 0x01, 0x02, 0x03, 0x00, 0x00, 0x00, 0x00])

    @patch('can.interfaces.virtual.VirtualBus.send')
    @patch('uds.CanTp.getNextBufferedMessage')
    # Test method to verify that CanTp sends a multi-frame message correctly for a small payload
    # Args:
    #    self: The instance of the test case class.
    #    getNextMessageMock: A mock object for the getNextReceivedMessage method.
    #    canSendMock: A mock object for the send method.
    # 1. Initializes an empty list 'result' to store the sent data and a counter 'count' to track message parts.
    # 2. Initializes a flag 'fcSent' to track if the flow control message is sent.
    
    # 3. Defines a function 'getNextMessage' to return specific messages to simulate flow control.
    #    Uses 'fcSent' flag to alternate the response between None and a flow control message.
    # 4. Defines a function 'msgData' to capture the message data sent by the mock and extend 'result' with message data.
    
    # 5. Sets 'getNextMessageMock' to return None, simulating no immediate response.
    # 6. Sets the side effect of 'canSendMock' to 'msgData' function to capture what is being sent.
    
    # 7. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 8. Sends a small payload list using the CanTp connection.
    # 9. Asserts that 'result' matches the expected multi-frame data after sending.
    def test_smallMultiFrameSend(self, getNextMessageMock, canSendMock):
    
            result = []
            count = 1
    
            fcSent = False
    
            def getNextMessage():
                nonlocal fcSent
                if not fcSent:
                    fcSent = True
                    return None
                else:
                    return can.Message(arbitration_id=0x600, data=[0x30, 0x00, 0x00])
    
            def msgData(msg):
                nonlocal result
                result.extend(msg.data)
    
            getNextMessageMock.return_value = None
            canSendMock.side_effect = msgData
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            tpConnection.send([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])
    
            self.assertEqual([0x10, 0x08, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x21, 0x07, 0x08, 0x00, 0x00, 0x00, 0x00,
                              0x00],
                             result)

    @patch('can.interfaces.virtual.VirtualBus.send')
    @patch('uds.CanTp.getNextBufferedMessage')
    # Test method to verify that CanTp sends a multi-frame message correctly for a larger payload
    # Args:
    #    self: The instance of the test case class.
    #    getNextMessageMock: A mock object for the getNextReceivedMessage method.
    #    canSendMock: A mock object for the send method.
    # 1. Initializes an empty list 'result' to store the sent data and a counter 'count' to track message parts.
    # 2. Initializes a flag 'fcSent' to track if the flow control message is sent.
    
    # 3. Defines a function 'getNextMessage' to return specific messages to simulate flow control.
    #    Uses 'fcSent' flag to alternate the response between None and a flow control message.
    # 4. Defines a function 'msgData' to capture the message data sent by the mock and extend 'result' with message data.
    
    # 5. Sets 'getNextMessageMock' to return None, simulating no immediate response.
    # 6. Sets the side effect of 'canSendMock' to 'msgData' function to capture what is being sent.
    
    # 7. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 8. Builds a larger payload list with elements ranging from 1 to 40.
    # 9. Sends the payload using the CanTp connection.
    # 10. Asserts that 'result' matches the expected multi-frame data after sending.
    def test_largerMultiFrameSend(self, getNextMessageMock, canSendMock):
    
            result = []
            count = 1
    
            fcSent = False
    
            def getNextMessage():
                nonlocal fcSent
                if not fcSent:
                    fcSent = True
                    return None
                else:
                    return can.Message(arbitration_id=0x600, data=[0x30, 0x00, 0x00])
    
            def msgData(msg):
                nonlocal result
                result.extend(msg.data)
    
            getNextMessageMock.return_value = None
            canSendMock.side_effect = msgData
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            payload = []
            for i in range(1, 41):
                payload.append(i)
    
            tpConnection.send(payload)
    
            self.assertEqual([0x10, 0x28, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06,
                              0x21, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D,
                              0x22, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14,
                              0x23, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A, 0x1B,
                              0x24, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21, 0x22,
                              0x25, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x00],
                             result)

    @patch('can.interfaces.virtual.VirtualBus.send')
    @patch('uds.CanTp.getNextBufferedMessage')
    # Test method to verify that CanTp sends a large multi-frame message correctly with multiple blocks
    # Args:
    #    self: The instance of the test case class.
    #    getNextMessageMock: A mock object for the getNextReceivedMessage method.
    #    canSendMock: A mock object for the send method.
    # 1. Initializes an empty list 'result' to store the sent data.
    # 2. Initializes 'blockSize' to 20 and 'cfCounter' to track consecutive frames sent.
    # 3. Initializes flags 'fcSent' to track if the flow control message is sent and 'ffSent_flag' to track if the first frame is sent.
    
    # 4. Defines a function 'getNextMessageFunc' to return specific messages to simulate flow control, using 'fcSent'.
    # 5. Defines a function 'msgData' to capture the message data sent by the mock, update the getNextMessageMock's side effect, and extend 'result' with message data.
    
    # 6. Sets 'getNextMessageMock' to return None, simulating no immediate response.
    # 7. Sets the side effect of 'canSendMock' to 'msgData' function to capture what is being sent.
    
    # 8. Initializes a payload list with elements ranging from 0 to 499.
    # 9. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 10. Sends the payload using the CanTp connection.
    
    # 11. Defines the expected result for the large multi-frame transmission and asserts that 'result' matches the expected data after sending.
    def test_canTpLargeMultiFrameWithMultipleBlocks(self, getNextMessageMock, canSendMock):
    
            result = []
            blockSize = 20
            cfCounter = 0
            fcSent = False
    
            ffSent_flag = False
    
            def getNextMessageFunc():
                nonlocal fcSent
                if fcSent is False:
                    fcSent = True
                    return [0x30, blockSize, 0x01]
    
                return None
    
            def msgData(msg):
                nonlocal getNextMessageMock
                nonlocal result
    
                getNextMessageMock.side_effect = getNextMessageFunc
                result += msg.data
    
            getNextMessageMock.return_value = None
            canSendMock.side_effect = msgData
    
            payload = []
            for i in range(0, 500):
                payload.append(i % 256)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            tpConnection.send(payload)
    
            expectedResult =   [0x11, 0xF4, 0x00, 0x01, 0x02, 0x03, 0x04, 0x05,
                                0x21, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C,
                                0x22, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13,
                                0x23, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A,
                                0x24, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21,
                                0x25, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
                                0x26, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F,
                                0x27, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,
                                0x28, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D,
                                0x29, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44,
                                0x2A, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B,
                                0x2B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52,
                                0x2C, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59,
                                0x2D, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60,
                                0x2E, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67,
                                0x2F, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E,
                                0x20, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75,
                                0x21, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C,
                                0x22, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83,
                                0x23, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A,
                                0x24, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91,
                                0x25, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98,
                                0x26, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F,
                                0x27, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6,
                                0x28, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD,
                                0x29, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4,
                                0x2A, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB,
                                0x2B, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xC2,
                                0x2C, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9,
                                0x2D, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0,
                                0x2E, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7,
                                0x2F, 0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE,
                                0x20, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5,
                                0x21, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC,
                                0x22, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3,
                                0x23, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA,
                                0x24, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF, 0x00, 0x01,
                                0x25, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                                0x26, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
                                0x27, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16,
                                0x28, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D,
                                0x29, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24,
                                0x2A, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B,
                                0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32,
                                0x2C, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39,
                                0x2D, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40,
                                0x2E, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
                                0x2F, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E,
                                0x20, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55,
                                0x21, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C,
                                0x22, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63,
                                0x23, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A,
                                0x24, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71,
                                0x25, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78,
                                0x26, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F,
                                0x27, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86,
                                0x28, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D,
                                0x29, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94,
                                0x2A, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B,
                                0x2B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA1, 0xA2,
                                0x2C, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9,
                                0x2D, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0,
                                0x2E, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7,
                                0x2F, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE,
                                0x20, 0xBF, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5,
                                0x21, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC,
                                0x22, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3,
                                0x23, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9, 0xDA,
                                0x24, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1,
                                0x25, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8,
                                0x26, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF,
                                0x27, 0xF0, 0xF1, 0xF2, 0xF3, 0x00, 0x00, 0x00]
    
            self.assertEqual(expectedResult, result)

    @patch('can.interfaces.virtual.VirtualBus.send')
    @patch('uds.CanTp.getNextBufferedMessage')
    # Test method to verify that CanTp sends a large multi-frame message correctly with changing block size during transmission
    # Args:
    #    self: The instance of the test case class.
    #    getNextMessageMock: A mock object for the getNextReceivedMessage method.
    #    canSendMock: A mock object for the send method.
    # 1. Initializes an empty list 'result' to store the sent data.
    # 2. Initializes 'blockSize' to 20 and 'cfCounter' to track consecutive frames sent.
    # 3. Initializes flags 'fcSent' to track if the flow control message is sent and 'ffSent_flag' to track if the first frame is sent.
    
    # 4. Defines a function 'getNextMessageFunc' to return specific messages to simulate flow control, using 'fcSent'. 
    #    - If 'fcSent' is False, returns a flow control frame with the block size and sets 'fcSent' to True.
    #    - If 'cfCounter' equals 'blockSize', resets the flow control state.
    # 5. Defines a function 'msgData' to capture the message data sent by the mock, update the getNextMessageMock's side effect,
    #    set the 'ffSent_flag' to True on first frame, and extend 'result' with message data. Increments 'cfCounter' with each sent frame.
    
    # 6. Sets 'getNextMessageMock' to return None, simulating no immediate response.
    # 7. Sets the side effect of 'canSendMock' to 'msgData' function to capture what is being sent.
    
    # 8. Initializes a payload list with elements ranging from 0 to 499.
    # 9. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 10. Sends the payload using the CanTp connection.
    
    # 11. Defines the expected result for the large multi-frame transmission with multiple block sizes and asserts that 'result' matches the expected data after sending.
    def test_canTpLargeMultiFrameWithMultipleBlockChangingBlockSizeDuringTransmission(self,
                                                                                          getNextMessageMock,
                                                                                          canSendMock):
    
            result = []
            blockSize = 20
            cfCounter = 0
            fcSent = False
    
            ffSent_flag = False
    
            def getNextMessageFunc():
                nonlocal fcSent
                nonlocal cfCounter
                nonlocal blockSize
                
                if fcSent is False:
                    fcSent = True
                    return [0x30, blockSize, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
                
                if cfCounter == blockSize:
                    fcSent = False
                    cfCounter = 0
                    
                if fcSent is True:
                    return None
    
            def msgData(msg):
                nonlocal getNextMessageMock
                nonlocal result
                nonlocal ffSent_flag
                nonlocal cfCounter
    
                if ffSent_flag is True:
                    cfCounter += 1
    
                if ffSent_flag is False:
                    ffSent_flag = True
                    getNextMessageMock.side_effect = getNextMessageFunc
    
                result += msg.data
    
            getNextMessageMock.return_value = None
            canSendMock.side_effect = msgData
    
            payload = []
            for i in range(0, 500):
                payload.append(i % 256)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            tpConnection.send(payload)
    
            expectedResult = [0x11, 0xF4, 0x00, 0x01, 0x02, 0x03, 0x04, 0x05,
                              0x21, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C,
                              0x22, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13,
                              0x23, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19, 0x1A,
                              0x24, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20, 0x21,
                              0x25, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28,
                              0x26, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F,
                              0x27, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36,
                              0x28, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D,
                              0x29, 0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44,
                              0x2A, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B,
                              0x2B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52,
                              0x2C, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59,
                              0x2D, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, 0x60,
                              0x2E, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67,
                              0x2F, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E,
                              0x20, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75,
                              0x21, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C,
                              0x22, 0x7D, 0x7E, 0x7F, 0x80, 0x81, 0x82, 0x83,
                              0x23, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A,
                              0x24, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91,
                              0x25, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97, 0x98,
                              0x26, 0x99, 0x9A, 0x9B, 0x9C, 0x9D, 0x9E, 0x9F,
                              0x27, 0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6,
                              0x28, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD,
                              0x29, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4,
                              0x2A, 0xB5, 0xB6, 0xB7, 0xB8, 0xB9, 0xBA, 0xBB,
                              0x2B, 0xBC, 0xBD, 0xBE, 0xBF, 0xC0, 0xC1, 0xC2,
                              0x2C, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9,
                              0x2D, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0,
                              0x2E, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7,
                              0x2F, 0xD8, 0xD9, 0xDA, 0xDB, 0xDC, 0xDD, 0xDE,
                              0x20, 0xDF, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4, 0xE5,
                              0x21, 0xE6, 0xE7, 0xE8, 0xE9, 0xEA, 0xEB, 0xEC,
                              0x22, 0xED, 0xEE, 0xEF, 0xF0, 0xF1, 0xF2, 0xF3,
                              0x23, 0xF4, 0xF5, 0xF6, 0xF7, 0xF8, 0xF9, 0xFA,
                              0x24, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF, 0x00, 0x01,
                              0x25, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
                              0x26, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F,
                              0x27, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16,
                              0x28, 0x17, 0x18, 0x19, 0x1A, 0x1B, 0x1C, 0x1D,
                              0x29, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24,
                              0x2A, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B,
                              0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32,
                              0x2C, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39,
                              0x2D, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, 0x40,
                              0x2E, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
                              0x2F, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E,
                              0x20, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55,
                              0x21, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C,
                              0x22, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63,
                              0x23, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A,
                              0x24, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71,
                              0x25, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78,
                              0x26, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F,
                              0x27, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86,
                              0x28, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D,
                              0x29, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94,
                              0x2A, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9A, 0x9B,
                              0x2B, 0x9C, 0x9D, 0x9E, 0x9F, 0xA0, 0xA1, 0xA2,
                              0x2C, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9,
                              0x2D, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0,
                              0x2E, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5, 0xB6, 0xB7,
                              0x2F, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD, 0xBE,
                              0x20, 0xBF, 0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5,
                              0x21, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC,
                              0x22, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3,
                              0x23, 0xD4, 0xD5, 0xD6, 0xD7, 0xD8, 0xD9, 0xDA,
                              0x24, 0xDB, 0xDC, 0xDD, 0xDE, 0xDF, 0xE0, 0xE1,
                              0x25, 0xE2, 0xE3, 0xE4, 0xE5, 0xE6, 0xE7, 0xE8,
                              0x26, 0xE9, 0xEA, 0xEB, 0xEC, 0xED, 0xEE, 0xEF,
                              0x27, 0xF0, 0xF1, 0xF2, 0xF3, 0x00, 0x00, 0x00]
    
            self.assertEqual(expectedResult, result)

    # Test method to verify that CanTp creates a block list correctly for a single block with a PDU that is not full
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with six elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 1.
    # 4. Asserts that the returned block list 'a' matches the expected structure with a single block and non-full PDU.
    def test_canTpCreateBlock_oneBlockSinglePduNotFull(self):
    
            testVal = []
            for i in range(0, 6):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 1)
    
            self.assertEqual(a, [[[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00]]])

    # Test method to verify that CanTp creates a block list correctly for a single block with a PDU that is full and matches the block size
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with seven elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 1.
    # 4. Asserts that the returned block list 'a' matches the expected structure with a single block and a full PDU that matches the block size.
    def test_canTpCreateBlock_oneBlockSinglePduFullSameAsBlockSize(self):
    
            testVal = []
            for i in range(0, 7):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 1)
    
            self.assertEqual(a, [[[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]]])

    # Test method to verify that CanTp creates a block list correctly for a single block with a full PDU that is smaller than the specified block size
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with seven elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 2.
    # 4. Asserts that the returned block list 'a' matches the expected structure with a single block and a full PDU, 
    #    even though the PDU size is smaller than the specified block size.
    def test_canTpCreateBlock_oneBlockSinglePduFullSmallerThanBlockSize(self):
    
            testVal = []
            for i in range(0, 7):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 2)
    
            self.assertEqual(a, [[[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]]])

    # Test method to verify that CanTp creates a block list correctly for a single block containing two PDUs with the second PDU not full
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with thirteen elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 2.
    # 4. Asserts that the returned block list 'a' matches the expected structure with a single block containing two PDUs,
    #    where the first PDU is full and the second PDU is not full.
    def test_canTpCreateBlock_oneBlockTwoPduNotFull(self):
            testVal = []
            for i in range(0, 13):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 2)
    
            self.assertEqual(a, [[[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00]]])

    # Test method to verify that CanTp creates a block list correctly for a single block containing two full PDUs
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with fourteen elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 2.
    # 4. Asserts that the returned block list 'a' matches the expected structure with a single block containing two full PDUs.
    def test_canTpCreateBlock_oneBlockTwoPduFull(self):
            testVal = []
            for i in range(0, 14):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 2)
    
            self.assertEqual(a, [[[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]]])

    # Test method to verify that CanTp creates a block list correctly for two blocks with two PDUs each, where the second PDU in the second block is not full
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with twenty-seven elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 2.
    # 4. Asserts that the returned block list 'a' matches the expected structure with two blocks:
    #    - The first block contains two full PDUs.
    #    - The second block contains one full PDU and one PDU that is not full.
    def test_canTpCreateBlock_twoBlockTwoPduNotFull(self):
            testVal = []
            for i in range(0, 27):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 2)
    
            self.assertEqual(a,
                             [
                                [[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]],
                                [[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x00]]
            ])

    # Test method to verify that CanTp creates a block list correctly for two blocks with two full PDUs each
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with twenty-eight elements, each set to 0xFF.
    # 2. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 3. Calls the 'create_blockList' method on the tpConnection with 'testVal' and block size of 2.
    # 4. Asserts that the returned block list 'a' matches the expected structure with two blocks:
    #    - Each block contains two full PDUs.
    def test_canTpCreateBlock_twoBlockTwoPduFull(self):
            testVal = []
            for i in range(0, 28):
                testVal.append(0xFF)
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 2)
    
            self.assertEqual(a,
                             [
                                [[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]],
                                [[0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF], [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]]
            ])

    # Test method to verify that CanTp creates a block list correctly for a case with no specific block size and a large PDU size
    # Args:
    #    self: The instance of the test case class.
    # 1. Initializes a 'testVal' list with four thousand and eighty-nine elements, each set to 0xFF.
    # 2. Initializes a 'result' list to hold the expected outcome, consisting of 584 full PDUs and one PDU that is not full.
    # 3. Initializes a CanTp connection with request ID 0x600 and response ID 0x650.
    # 4. Calls the 'create_blockList' method on the tpConnection with 'testVal' and a large block size of 585.
    # 5. Asserts that the first block in the returned block list 'a' matches the expected 'result'.
    def test_canTpCreateBlock_noBlockSizePdu(self):
            testVal = []
            for i in range(0, 4089):
                testVal.append(0xFF)
    
            result = []
            for i in range(584):
                result.append([0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
    
            result.append([0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    
            tpConnection = CanTp(reqId=0x600, resId=0x650)
    
            a = tpConnection.create_blockList(testVal, 585)
    
            self.assertEqual(a[0],
                             result)


if __name__ == "__main__":
    unittest.main()
