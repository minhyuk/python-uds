"""
This script defines a `RequestDownloadContainer` class that serves as a container for handling the Request Download service in the context of UDS (Unified Diagnostic Services).

Key Components:
1. __init__ method: Initializes dictionaries to store request functions, check functions, negative response functions, and positive response functions.

2. __requestDownload method: Handles the Request Download service by sending a request to download data based on the Format Identifier, Memory Address, and Memory Size provided. It then processes the response received from the target by calling appropriate check and response functions.

3. bind_function method: Binds the __requestDownload method to an external Uds object to allow it to be called as an in-built method for initiating the Request Download service.

4. add_requestFunction, add_checkFunction, add_negativeResponseFunction, add_positiveResponseFunction methods: Allows adding specific functions related to Request Download service to the respective dictionaries for further processing.

Overall, this script encapsulates the functionality to perform the Request Download service in a standardized manner by managing request, response, and validation actions within the RequestDownloadContainer class.
"""
