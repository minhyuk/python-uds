#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import cProfile
import sys
from functools import reduce


# ----------------------------------------------------------------
# Profiler Code
# ----------------------------------------------------------------
# Decorator function to profile another function using cProfile
# Args:
#    func: The function to be profiled.
# 1. Defines an inner function 'profiled_func' that will be the profiled version of 'func'.
#    - This inner function will call 'cProfile.runctx' to run 'func' within a profiling context.
# 2. Returns the 'profiled_func' function, effectively replacing 'func' with its profiled version.
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        import cProfile, pstats, io
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return result
    return profiled_func

# ----------------------------------------------------------------
# buildIntFromList Tests
# ----------------------------------------------------------------


@do_cprofile
# Function to build an integer from a list of integers representing its digits.
# Args:
#    aList: A list of integers where each integer is a digit in the final number.
# 1. Defines an inner function 'buildIntFromList' that will perform the actual conversion of the list to an integer.
# 2. Calls the 'buildIntFromList' function with 'aList' and returns the result.
def buildIntFromListNonRecursiveFunc(aList):
    def buildIntFromList(aList):
        number = 0
        for digit in aList:
            number = number * 10 + digit
        return number
    return buildIntFromList(aList)


@do_cprofile
# Function to build an integer from a list of integers representing its digits using a recursive approach.
# Args:
#    aList: A list of integers where each integer is a byte in the final number.
# 1. Defines an inner recursive function 'buildIntFromList' that will perform the actual conversion of the list to an integer.
#    - The base case: if the list is empty, return 0.
#    - The recursive case: process the first element and recursively call the function for the rest of the list.
# 2. Calls the 'buildIntFromList' function with 'aList' and returns the result.
def buildIntFromListRecursiveFunc(aList):
    def buildIntFromList(aList):
        if not aList:
            return 0
        return (aList[0] << (8 * (len(aList) - 1))) + buildIntFromList(aList[1:])
        
    return buildIntFromList(aList)


@do_cprofile
# Function to build an integer from a list of integers representing its digits using the reduce function.
# Args:
#    aList: A list of integers where each integer is a byte in the final number.
# 1. Defines an inner function 'buildIntFromList' that will perform the conversion of the list to an integer using the reduce method.
#    - Uses functools.reduce to apply a lambda function that shifts the accumulated result left by 8 bits and adds the current digit.
# 2. Calls the 'buildIntFromList' function with 'aList' and returns the result.
def buildIntFromListReduceFunc(aList):
    from functools import reduce

    def buildIntFromList(aList):
        return reduce(lambda acc, digit: (acc << 8) + digit, aList, 0)
    
    return buildIntFromList(aList)


# ----------------------------------------------------------------
# byteListToString Tests
# ----------------------------------------------------------------


@do_cprofile
# Function to convert a list of bytes to a string using a non-recursive approach.
# Args:
#    aList: A list of integers representing byte values.
# 1. Defines an inner function 'byteListToString' that will perform the actual conversion of the list to a string.
#    - Joins the list of byte values into a string by converting each byte to its corresponding character.
# 2. Calls the 'byteListToString' function with 'aList' and returns the result.
def byteListToStringNonRecursiveFunc(aList):
    def byteListToString(aList):
        return ''.join(map(chr, aList))
    
    return byteListToString(aList)


@do_cprofile
# Function to convert a list of bytes to a string using a recursive approach.
# Args:
#    aList: A list of integers representing byte values.
# 1. Defines an inner recursive function 'byteListToString' that will perform the actual conversion of the list to a string.
#    - The base case: If the list is empty, return an empty string.
#    - The recursive case: Convert the first element of the list to its corresponding character and concatenate it with the result of processing the rest of the list.
# 2. Calls the 'byteListToString' function with 'aList' and returns the result.
def byteListToStringRecursiveFunc(aList):
    def byteListToString(aList):
        if not aList:
            return ""
        return chr(aList[0]) + byteListToString(aList[1:])
    
    return byteListToString(aList)


@do_cprofile
# Function to convert a list of bytes to a string using the reduce function.
# Args:
#    aList: A list of integers representing byte values.
# 1. Defines an inner function 'byteListToString' that will perform the actual conversion of the list to a string using functools.reduce.
#    - Uses functools.reduce to apply a lambda function that concatenates the accumulated string with the character corresponding to the current byte.
# 2. Calls the 'byteListToString' function with 'aList' and returns the result.
def byteListToStringReduceFunc(aList):
    from functools import reduce
    
    def byteListToString(aList):
        return reduce(lambda acc, byte: acc + chr(byte), aList, "")
    
    return byteListToString(aList)


if __name__ == "__main__":

    sys.setrecursionlimit(4000)

    testListA = []
    for i in range(0, 2500):
        testListA.append(0x5a)

    testListB = []
    for i in range(0, 2500):
        testListB.append(0x30)

    print("Testing the buildIntFromList methods")
    resultA = buildIntFromListNonRecursiveFunc(testListA)
    resultB = buildIntFromListRecursiveFunc(testListA)
    resultC = buildIntFromListReduceFunc(testListA)

    assert(resultA == resultB == resultC)

    print("Testing the byteListToString methods")
    resultA = byteListToStringNonRecursiveFunc(testListB)
    resultB = byteListToStringRecursiveFunc(testListB)
    resultC = byteListToStringReduceFunc(testListB)

    assert (resultA == resultB == resultC)
    pass
