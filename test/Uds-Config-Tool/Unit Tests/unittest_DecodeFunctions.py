#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


from uds.uds_config_tool import DecodeFunctions
import unittest


class CanTpMessageTestCase(unittest.TestCase):

    # Test method to verify that extracting a bit from byte position 0 returns True when the bit is set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x01, representing a byte where the least significant bit (position 0) is set to 1.
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 0 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is True, indicating that the bit at position 0 is correctly identified as set.
    def testBitExtractFromBytePos0True(self):
            testVal = 0x01
            result = DecodeFunctions.extractBitFromPosition(testVal, 0)
            self.assertEqual(True, result)

    # Test method to verify that extracting a bit from byte position 0 returns False when the bit is not set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x00, representing a byte where the least significant bit (position 0) is set to 0.
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 0 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is False, indicating that the bit at position 0 is correctly identified as not set.
    def testBitExtractFromBytePos0False(self):
            testVal = 0x00
            result = DecodeFunctions.extractBitFromPosition(testVal, 0)
            self.assertEqual(False, result)

    # Test method to verify that extracting a bit from byte position 1 returns True when the bit is set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x02, representing a byte where the bit at position 1 is set to 1 (binary: 00000010).
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 1 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is True, indicating that the bit at position 1 is correctly identified as set.
    def testBitExtractFromBytePos1True(self):
            testVal = 0x02
            result = DecodeFunctions.extractBitFromPosition(testVal, 1)
            self.assertEqual(True, result)

    # Test method to verify that extracting a bit from byte position 1 returns False when the bit is not set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x00, representing a byte where the bit at position 1 is set to 0.
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 1 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is False, indicating that the bit at position 1 is correctly identified as not set.
    def testBitExtractFromBytePos1False(self):
            testVal = 0x00
            result = DecodeFunctions.extractBitFromPosition(testVal, 1)
            self.assertEqual(False, result)

    # Test method to verify the extraction of multiple bits from different positions in a byte
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x5A, representing a byte with a specific bit pattern (binary: 01011010).
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 0 from 'testVal'. 
    #    - Asserts that the result is False, indicating the bit is not set.
    # 3. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 1 from 'testVal'. 
    #    - Asserts that the result is True, indicating the bit is set.
    # 4. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 2 from 'testVal'. 
    #    - Asserts that the result is False, indicating the bit is not set.
    # 5. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 3 from 'testVal'. 
    #    - Asserts that the result is True, indicating the bit is set.
    # 6. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 4 from 'testVal'. 
    #    - Asserts that the result is True, indicating the bit is set.
    # 7. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 5 from 'testVal'. 
    #    - Asserts that the result is False, indicating the bit is not set.
    # 8. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 6 from 'testVal'. 
    #    - Asserts that the result is True, indicating the bit is set.
    # 9. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 7 from 'testVal'. 
    #    - Asserts that the result is False, indicating the bit is not set.
    
    def testMultipleBitExtractFromByte(self):
            testVal = 0x5A
            result = DecodeFunctions.extractBitFromPosition(testVal, 0)
            self.assertEqual(False, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 1)
            self.assertEqual(True, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 2)
            self.assertEqual(False, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 3)
            self.assertEqual(True, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 4)
            self.assertEqual(True, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 5)
            self.assertEqual(False, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 6)
            self.assertEqual(True, result)
            result = DecodeFunctions.extractBitFromPosition(testVal, 7)
            self.assertEqual(False, result)

    # Test method to verify that extracting a bit from word position 8 returns True when the bit is set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x100, representing a word where the bit at position 8 is set to 1 (binary: 0000000100000000).
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 8 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is True, indicating that the bit at position 8 is correctly identified as set.
    def testBitExtractFromWordPos8True(self):
            testVal = 0x100
            result = DecodeFunctions.extractBitFromPosition(testVal, 8)
            self.assertEqual(True, result)

    # Test method to verify that extracting a bit from word position 8 returns False when the bit is not set
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0x000, representing a word where the bit at position 8 is set to 0.
    # 2. Calls the 'extractBitFromPosition' method on 'DecodeFunctions' to extract the bit at position 8 from 'testVal'.
    # 3. Asserts that the result of 'extractBitFromPosition' is False, indicating that the bit at position 8 is correctly identified as not set.
    def testBitExtractFromWordPos8False(self):
            testVal = 0x000
            result = DecodeFunctions.extractBitFromPosition(testVal, 8)
            self.assertEqual(False, result)

    # Test method to verify the extraction of a 4-bit integer from position 0 of an 8-bit integer
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0xA5, representing an 8-bit integer (binary: 10100101).
    # 2. Calls the 'extractIntFromPosition' method on 'DecodeFunctions' to extract a 4-bit integer starting at position 0 from 'testVal'.
    # 3. Asserts that the result of 'extractIntFromPosition' is 0x05, indicating that the 4 bits starting at position 0 are correctly extracted (binary: 0101).
    def test4BitIntExtractFromPos0Of8BitInt(self):
            testVal = 0xA5
            result = DecodeFunctions.extractIntFromPosition(testVal, 4, 0)
            self.assertEqual(0x05, result)

    # Test method to verify the extraction of a 4-bit integer from position 1 of an 8-bit integer
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0xA5, representing an 8-bit integer (binary: 10100101).
    # 2. Calls the 'extractIntFromPosition' method on 'DecodeFunctions' to extract a 4-bit integer starting at position 1 from 'testVal'.
    # 3. Asserts that the result of 'extractIntFromPosition' is 0x2, indicating that the 4 bits starting at position 1 are correctly extracted (binary: 0010).
    def test4BitIntExtractFromPos1Of8BitInt(self):
            testVal = 0xA5
            result = DecodeFunctions.extractIntFromPosition(testVal, 4, 1)
            self.assertEqual(0x2, result)

    # Test method to verify the extraction of a 4-bit integer from position 2 of an 8-bit integer
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0xA5, representing an 8-bit integer (binary: 10100101).
    # 2. Calls the 'extractIntFromPosition' method on 'DecodeFunctions' to extract a 4-bit integer starting at position 2 from 'testVal'.
    # 3. Asserts that the result of 'extractIntFromPosition' is 0x9, indicating that the 4 bits starting at position 2 are correctly extracted (binary: 1001).
    def test4BitIntExtractFromPos2Of8BitInt(self):
            testVal = 0xA5
            result = DecodeFunctions.extractIntFromPosition(testVal, 4, 2)
            self.assertEqual(0x9, result)

    # Test method to verify the extraction of a 6-bit integer from position 2 of an 8-bit integer
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to 0xA5, representing an 8-bit integer (binary: 10100101).
    # 2. Calls the 'extractIntFromPosition' method on 'DecodeFunctions' to extract a 6-bit integer starting at position 2 from 'testVal'.
    # 3. Asserts that the result of 'extractIntFromPosition' is 0x29, indicating that the 6 bits starting at position 2 are correctly extracted (binary: 101001).
    def test6BitIntExtractFromPos2Of8BitInt(self):
            testVal = 0xA5
            result = DecodeFunctions.extractIntFromPosition(testVal, 6, 2)
            self.assertEqual(0x29, result)

    # Test method to verify the construction of an integer from a 1-byte array
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to [0x5A], representing a list with a single byte (0x5A).
    # 2. Calls the 'buildIntFromList' method on 'DecodeFunctions' to construct an integer from 'testVal'.
    # 3. Asserts that the result of 'buildIntFromList' is 0x5A, indicating that the single-byte list is correctly converted to an integer.
    def testBuildIntFromArray1ByteArray(self):
            testVal = [0x5A]
            result = DecodeFunctions.buildIntFromList(testVal)
            self.assertEqual(0x5A, result)

    # Test method to verify the construction of an integer from a 2-byte array
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to [0x5A, 0xA5], representing a list with two bytes (0x5A and 0xA5).
    # 2. Calls the 'buildIntFromList' method on 'DecodeFunctions' to construct an integer from 'testVal'.
    # 3. Asserts that the result of 'buildIntFromList' is 0x5AA5, indicating that the two-byte list is correctly converted to an integer.
    def testBuildIntFromArray2ByteArray(self):
            testVal = [0x5A, 0xA5]
            result = DecodeFunctions.buildIntFromList(testVal)
            self.assertEqual(0x5AA5, result)

    # Test method to verify the construction of an integer from a 3-byte array
    # Args:
    #    self: The instance of the test case class.
    # 1. Sets testVal to [0x5A, 0xA5, 0x5A], representing a list with three bytes (0x5A, 0xA5, and 0x5A).
    # 2. Calls the 'buildIntFromList' method on 'DecodeFunctions' to construct an integer from 'testVal'.
    # 3. Asserts that the result of 'buildIntFromList' is 0x5AA55A, indicating that the three-byte list is correctly converted to an integer.
    def testBuildIntFromArray3ByteArray(self):
            testVal = [0x5A, 0xA5, 0x5A]
            result = DecodeFunctions.buildIntFromList(testVal)
            self.assertEqual(0x5AA55A, result)

    def testBuildIntFromArray4ByteArray(self):
            testVal = [0x5A, 0xA5, 0xA5, 0x5A]
            result = DecodeFunctions.buildIntFromList(testVal)
            self.assertEqual(0x5AA5A55A, result)

    def testBuildIntFromArray8ByteArray(self):
            testVal = [0x5A, 0xa5, 0xA5, 0x5A, 0x5A, 0xA5, 0xA5, 0x5A]
            result = DecodeFunctions.buildIntFromList(testVal)
            self.assertEqual(0x5AA5A55A5AA5A55A, result)

    def testStringToByteArrayAlphaOnlyAscii(self):
            testVal = 'abcdefghijklmn'
            result = DecodeFunctions.stringToIntList(testVal, 'ascii')
            self.assertEqual([0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E], result)

    def testStringToByteArrayNumericOnlyAscii(self):
            testVal = 'abcdefg01234'
            result = DecodeFunctions.stringToIntList(testVal, 'ascii')
            self.assertEqual([0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x30, 0x31, 0x32, 0x33, 0x34], result)

    def testStringToByteArrayAlphaOnlyUtf8(self):
            testVal = 'abcdefg'
            result = DecodeFunctions.stringToIntList(testVal, 'utf-8')
            self.assertEqual([0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67], result)

    def testByteArrayToStringAlphaOnlyAscii(self):
            testVal = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E]
            result = DecodeFunctions.intListToString(testVal, 'ascii')
            self.assertEqual('abcdefghijklmn', result)

    def testUint16ArrayToUint8Array(self):
            testVal = [0x5AA5, 0xA55A]
            result = DecodeFunctions.intArrayToUInt8Array(testVal, 'int16')
            self.assertEqual([0x5a, 0xA5, 0xA5, 0x5A], result)

    def testUint8ArraytoUint16Array(self):
            testVal = [0x5aa55aa5, 0xa55aa55a]
            result = DecodeFunctions.intArrayToUInt8Array(testVal, 'int32')
            self.assertEqual([0x5a, 0xa5, 0x5a, 0xa5, 0xA5, 0x5A, 0xa5, 0x5a], result)

if __name__ == "__main__":
    unittest.main()