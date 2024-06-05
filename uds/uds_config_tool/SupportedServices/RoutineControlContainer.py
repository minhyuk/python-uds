"""
This script defines the `RoutineControlContainer` class, which contains functions related to controlling routines in the Unified Diagnostic Services (UDS) protocol. The class includes methods for binding functions to an external object, adding request, check, negative response, and positive response functions related to the Routine Control service.

The class implements a static method named `__routineControl` that handles the routine control based on the provided routine parameter, control type, option record, and whether the response should be suppressed. It constructs the request by calling the appropriate request function, sends the request, receives the response, and validates it based on the expected responses and data provided. The method also includes checks for negative responses and processes positive responses accordingly.

Furthermore, the class provides methods to add various functions to the container, such as functions for handling requests, checks, negative responses, and positive responses related to routine control. These methods allow for customizing the processing of data in the Routine Control service.

Overall, this class manages the operations related to controlling routines in the UDS protocol, ensuring requests are correctly formed, responses are validated, and appropriate actions are taken based on the response received.
"""
