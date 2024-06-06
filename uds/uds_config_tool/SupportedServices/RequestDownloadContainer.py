"""
This module defines the `RequestDownloadContainer` class that handles the request download feature in the UDS (Unified Diagnostic Services) protocol.

Attributes:
    __metaclass__: Metaclass to use the `iContainer` as the base metaclass.
    requestFunctions: A dictionary to hold different types of request functions.
    checkFunctions: A dictionary to hold different check functions.
    negativeResponseFunctions: A dictionary to hold functions for handling negative responses.
    positiveResponseFunctions: A dictionary to hold functions for handling positive responses.

Methods:
    __requestDownload: Handles the request download functionality by generating the request, sending it, and processing the response.
    bind_function: Binds the `requestDownload` method to an external UDS object.
    add_requestFunction: Adds a request function to the container.
    add_checkFunction: Adds a check function to the container.
    add_negativeResponseFunction: Adds a function to handle negative responses to the container.
    add_positiveResponseFunction: Adds a function to handle positive responses to the container.
"""
"""
