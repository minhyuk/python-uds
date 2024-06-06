"""
This module contains factory methods for handling the Transfer Exit service element, including creating the request function, checking the positive response, encoding the positive response, and checking the negative response.
The module also includes templates for the request function, check function, negative response function, and positive response encoding function.

Attributes:
    __author__: The author of the code.
    __copyrights__: Copyright information for the project.
    __credits__: List of contributors or individuals credited for the project.
    __license__: The license under which the project is distributed.
    __maintainer__: The maintainer of the project.
    __email__: Contact email for the maintainer.
    __status__: The current status of the project (e.g., Development, Production).

Note:
    This module provides methods for efficient handling of the Transfer Exit service element in a structured manner.
"""

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]
__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"

"""
Template for creating the request function.
"""
requestFuncTemplate = str("def {0}(parameterRecord):\n"
                          "    output = {1}\n"
                          "    if parameterRecord is not None: output += parameterRecord\n"
                          "    return output")

"""
Template for creating the check function for positive response.
"""
checkFunctionTemplate = str("def {0}(input):\n"
                            "    serviceIdExpected = {1}\n"
                            "    serviceId = DecodeFunctions.buildIntFromList(input[{2}:{3}])\n"
                            "    if(serviceId != serviceIdExpected): raise Exception(\"Service Id Received not expected. Expected {{0}}; Got {{1}} \".format(serviceIdExpected, serviceId))")

"""
Template for creating the negative response function.
"""
negativeResponseFuncTemplate = str("def {0}(input):\n"
                                   "    {1}")

"""
Template for encoding the positive response.
"""
encodePositiveResponseFuncTemplate = str("def {0}(input):\n"
                                         "    result = {{}}\n"
                                         "    result['transferResponseParameterRecord']= input[1:]\n"
                                         "    return result")
