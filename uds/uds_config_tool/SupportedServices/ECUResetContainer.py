"""
This script defines the `ECUResetContainer` class, which contains functions related to the ECU Reset service in the Unified Diagnostic Services (UDS) protocol. It includes methods for binding functions to an external object, adding request, check, negative response, and positive response functions related to the ECU Reset service.

The class implements a static method named `__ecuReset` that handles ECU Reset actions. It sends a request for ECU Reset, receives the response, and validates the response. The method also includes checks for suppressResponse to handle cases where the response should be suppressed or processed. Additionally, it binds this method to an external Uds object for execution.

Overall, this class manages the operations related to the ECU Reset service in the UDS protocol, ensuring that ECU Reset actions are appropriately handled and responses are processed according to the UDS specifications.
"""
