"""
This module contains factory methods to handle the ReadDTC service element, including creating the request function, checking the positive response, encoding the positive response, and checking the negative response. It also includes templates for the request function, check function, negative response function, and positive response encoding function.

Attributes:
    __author__: The author of the code.
    __copyrights__: Copyright information for the project.
    __credits__: List of contributors or individuals credited for the project.
    __license__: The license under which the project is distributed.
    __maintainer__: The maintainer of the project.
    __email__: Contact email for the maintainer.
    __status__: The current status of the project (e.g., Development, Production).

Note:
    This module contains methods for creating and handling the ReadDTC service element in a structured manner.
"""

"""Template for creating the request function."""
requestFuncTemplate = str("def {0}(DTCStatusMask=[],DTCMaskRecord=[],DTCSnapshotRecordNumber=[],DTCExtendedRecordNumber=[],DTCSeverityMask=[]):\n"
                          "    encoded = []\n"
                          "    {3}\n"
                          "    return {1} + {2} + encoded # ... SID, sub-func, and params")

"""Template for creating the check function for positive response."""
checkFunctionTemplate = str("def {0}(input):\n"
                            "    serviceIdExpected = {1}\n"
                            "    subFunctionExpected = {2}\n"
                            "    serviceId = DecodeFunctions.buildIntFromList(input[{3}:{4}])\n"
                            "    subFunction = DecodeFunctions.buildIntFromList(input[{5}:{6}])\n"
                            "    if(serviceId != serviceIdExpected): raise Exception(\"Service Id Received not expected. Expected {{0}}; Got {{1}} \".format(serviceIdExpected, serviceId))\n"
                            "    if(subFunction != subFunctionExpected): raise Exception(\"Sub-function Received not expected. Expected {{0}}; Got {{1}}\".format(subFunctionExpected, subFunction))\n"
                            "{7}")

"""Template for creating the negative response function."""
negativeResponseFuncTemplate = str("def {0}(input):\n"
                                   "    {1}")

"""Template for encoding the positive response."""
encodePositiveResponseFuncTemplate = str("def {0}(input):\n"
                                         "    encoded = []\n"
                                         "    retval = None\n"
                                         "{1}\n"
                                         "    return retval")

