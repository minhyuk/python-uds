"""
This module defines an abstract base class for Transport Protocols (Tp) used in the python-uds project.

Attributes:
- __author__ (str): The author of the module.
- __copyrights__ (str): The copyright information of the module.
- __credits__ (list): The list of credits for the module.
- __license__ (str): The license information of the module.
- __maintainer__ (str): The maintainer of the module.
- __email__ (str): The email address for contacting the module maintainer.
- __status__ (str): The development status of the module.

Abstract Methods:
- send: An abstract method for sending a payload.
- recv: An abstract method for receiving data within a specific timeout.
- closeConnection: An abstract method for closing the connection.

"""
