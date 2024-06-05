"""
This script consists of a collection of test cases for validating the ECU Reset functionality in the UDS protocol. The test suite focuses on the 'routineControl' function with various routine control types and parameters to simulate ECU reset operations, such as erasing memory, starting routines, checking application status, and requesting routine results.

Each test method is designed to patch the sending and receiving messages for the CanTp communication layer, ensuring that the ECU reset operations are triggered correctly and handle positive and negative responses appropriately. 

Notable Features:
- Tests for routine control functionalities like starting routines, stopping routines, and requesting routine results.
- Tests are segmented based on different routine control types and scenario variations to ensure comprehensive test coverage.

Test Methods:
1. The 'test_routineControlRequestDfltNoSuppress' method validates the startRoutine with the default suppress setting.
2. The 'test_routineControlRequestNoSuppress' method checks the startRoutine operation without suppressing the response.
3. Other test methods cover different routine control scenarios such as stopping routines, requesting results, and checking application status.

Negative Response Handling:
- The script includes test cases to handle negative responses like 0x12, 0x13, 0x22, 0x24, 0x31, 0x33, and 0x72 during ECU reset operations, providing exception reporting when negative responses are detected.

Please refer to the individual test method docstrings and comments within the script for detailed information on each test case and the specific routine control operation being examined.
"""
"""
