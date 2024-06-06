"""
This module defines the `RoutineControlContainer` class, which manages the request, check, and response functions related to the Routine Control service.
It provides a static method `__routineControl` to handle the Routine Control request-response action for different parameters, control types, and option records.

Attributes:
    __metaclass__: Metaclass for the `RoutineControlContainer` class.
    requestFunctions: Dictionary to store request functions based on different parameter and control types for the Routine Control service.
    checkFunctions: Dictionary to store check functions based on different parameter and control types for the Routine Control service.
    negativeResponseFunctions: Dictionary to store functions to handle negative responses for the Routine Control service.
    positiveResponseFunctions: Dictionary to store functions to handle positive responses for the Routine Control service.

Methods:
    - __routineControl: Static method to execute the Routine Control request-response action for given parameters, control types, and option records.
    - bind_function: Binds the methods to an external object.
    - add_requestFunction: Adds a request function to the RoutineControlContainer based on the dictionary entry.
    - add_checkFunction: Adds a check function to the RoutineControlContainer based on the dictionary entry.
    - add_negativeResponseFunction: Adds a function to handle negative responses to the RoutineControlContainer based on the dictionary entry.
    - add_positiveResponseFunction: Adds a function to handle positive responses to the RoutineControlContainer based on the dictionary entry.
"""
