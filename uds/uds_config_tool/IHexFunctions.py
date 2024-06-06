"""
This script contains classes and functions for parsing and processing Intel Hex (IHEX) files.

Classes:
- ihexRecordType: Enumerates the record types in an IHEX file.
- ihexData: Represents the data records in an IHEX file.
- ihexFile: Represents an entire IHEX file and contains methods for processing the file.

Functions:
- extractBitFromPosition(aInt, position): Extracts a bit from a specified position in an integer.
- extractIntFromPosition(aInt, size, position): Extracts an integer from a specified position with a given size.
- buildIntFromList(aList): Concatenates a list of integers into a single integer using the reduce pattern.
- stringToIntList(aString, encodingType): Converts a string into a list of integer values.
- intListToString(aList, encodingType): Converts a list of integers to a string.
- intArrayToUInt8Array(aArray, inputType): Converts an array of integers to an array of unsigned 8-bit integers.
- intArrayToIntArray(aArray, inputType, outputType): Converts an array of integers from one type to another.

This script can be used to read, parse, and process Intel Hex files, as well as interact with the data records in the file.

Example Usage:
- Load an IHEX file using ihexFile class and support operations like transferring data to a target device.
"""
