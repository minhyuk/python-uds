"""
This module defines the `ECUResetContainer` class, which manages the request, check, negative response, and positive response functions related to ECU reset services. 
It includes a static method `__ecuReset` to handle the ECU reset request-response action. 

Attributes:
    __metaclass__: Metaclass for the `ECUResetContainer` class.
    requestFunctions: Dictionary to store request functions for the ECU reset service.
    checkFunctions: Dictionary to store check functions for the ECU reset service.
    negativeResponseFunctions: Dictionary to store functions to handle negative responses for the ECU reset service.
    positiveResponseFunctions: Dictionary to store functions to handle positive responses for the ECU reset service.

Methods:
    - __ecuReset: Static method to execute the ECU reset request-response action. 
    - bind_function: Binds the methods to an external object.
    - add_requestFunction: Adds a request function to the ECUResetContainer.
    - add_checkFunction: Adds a check function to the ECUResetContainer.
    - add_negativeResponseFunction: Adds a function to handle negative responses to the ECUResetContainer.
    - add_positiveResponseFunction: Adds a function to handle positive responses to the ECUResetContainer.
"""
