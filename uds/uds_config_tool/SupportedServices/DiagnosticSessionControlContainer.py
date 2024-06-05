"""
This script defines the `DiagnosticSessionControlContainer` class that holds functions related to the Diagnostic Session Control service in Unified Diagnostic Services (UDS) protocol. It includes methods for binding functions to an external Uds object, adding request, check, negative response, and positive response functions related to the Diagnostic Session Control service. It also includes static methods to handle the diagnostic session control actions like session control, tester present behavior, time tracking for the last send message, and setting last send time.

The class includes functions to handle the diagnostic session control by executing requests and responses in specified service types. It also manages the Tester Present option by setting the required parameters based on specific diagnostic session types. Additionally, the script provides methods for keeping track of the time elapsed since the last message was sent for the current session.

Note: The functions in this class are related to the specific services for diagnostic session control and tester present behavior.
"""
