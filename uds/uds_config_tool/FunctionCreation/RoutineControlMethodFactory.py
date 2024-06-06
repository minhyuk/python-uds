"""
This module contains factory methods to handle the Routine Control service element, including creating the request function, checking the positive response, encoding the positive response, and checking the negative response. It also includes templates for the request function, check function, negative response function, and positive response encoding function.

Attributes:
    __author__: The author of the code.
    __copyrights__: Copyright information for the project.
    __credits__: List of contributors or individuals credited for the project.
    __license__: The license under which the project is distributed.
    __maintainer__: The maintainer of the project.
    __email__: Contact email for the maintainer.
    __status__: The current status of the project (e.g., Development, Production).
    SUPPRESS_RESPONSE_BIT: Constant value for the suppress response bit.

Note:
    This module contains methods for creating and handling the Routine Control service element in a structured manner.
"""

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]
__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"

"""Template for creating the request function."""
requestFuncTemplate = str("def {0}(optionRecord,suppressResponse=False):\n"
                          "    controlType = {2}\n"
                          "    suppressBit = {6} if suppressResponse else 0x00\n"
                          "    controlType[0] += suppressBit\n"
                          "    encoded = []\n"
                          "    if optionRecord is not None:\n"
                          "        if type(optionRecord) == list and type(optionRecord[0]) == tuple:\n"
                          "            drDict = dict(optionRecord)\n"
                          "            {4}\n"
                          "{5}\n"
                          "    return {1} + controlType + {3} + encoded")


"""Template for creating the check function for positive response."""
checkFunctionTemplate = str("def {0}(input):\n"
                            "    serviceIdExpected = {1}\n"
                            "    controlTypeExpected = {2}\n"
                            "    routineIdExpected = {3}\n"
                            "    serviceId = DecodeFunctions.buildIntFromList(input[{4}:{5}])\n"
                            "    controlType = DecodeFunctions.buildIntFromList(input[{6}:{7}])\n"
                            "    routineId = DecodeFunctions.buildIntFromList(input[{8}:{9}])\n"
                            "    if(len(input) != {10}): raise Exception(\"Total length returned not as expected. Expected: {10}; Got {{0}}\".format(len(input)))\n"
                            "    if(serviceId != serviceIdExpected):raise Exception(\"Service Id Received not expected. Expected {{0}}; Got {{1}}\".format(serviceIdExpected, serviceId))\n"
                            "    if(controlType != controlTypeExpected):raise Exception(\"Control Type Received not expected. Expected {{0}}; Got {{1}}\".format(controlTypeExpected, controlType))\n"
                            "    if(routineId != routineIdExpected):raise Exception(\"Routine Id Received not as expected. Expected: {{0}}; Got {{1}}\".format(routineIdExpected, routineId))")

"""Template for creating the negative response function."""
negativeResponseFuncTemplate = str("def {0}(input):\n"
                                   "    {1}")

"""Template for encoding the positive response."""
encodePositiveResponseFuncTemplate = str("def {0}(input):\n"
                                         "    result = {{}}\n"
                                         "{1}\n"
                                         "    return result")
