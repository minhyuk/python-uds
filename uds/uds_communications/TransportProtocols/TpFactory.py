"""
This module provides a TpFactory class for creating different types of Transport Protocol objects.

Attributes:
- __author__ (str): The author of the module.
- __copyrights__ (str): The copyright information of the module.
- __credits__ (list): The list of credits for the module.
- __license__ (str): The license information of the module.
- __maintainer__ (str): The maintainer of the module.
- __email__ (str): The email address for contacting the module maintainer.
- __status__ (str): The development status of the module.

Classes:
- TpFactory: A class for creating different Transport Protocol objects.

Methods:
- __call__: A method of the TpFactory class to create specific types of Transport Protocol objects based on the given type.
- loadConfiguration: A method to load the configuration settings.

Raises:
- NotImplementedError: If the requested transport type is not supported.
- Exception: If an unknown transport type is selected.
- FileNotFoundError: If the specified configuration file is not found.
"""
