"""
This module contains a custom Config class that inherits from ConfigParser, used for parsing configuration files.

Attributes:
    __author__: The author of the code.
    __copyrights__: Copyright information for the project.
    __credits__: List of contributors or individuals credited for the project.
    __license__: The license under which the project is distributed.
    __maintainer__: The maintainer of the project.
    __email__: Contact email for the maintainer.
    __status__: The current status of the project (e.g., Development, Production).

Note:
    This class provides extended functionality to ConfigParser for handling configuration files.
"""

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]
__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"

class Config(ConfigParser):
    """
    A custom configuration parser class that extends ConfigParser.

    Inherits:
        ConfigParser: The default configuration parser class.

    Methods:
        __init__: Constructor method for the Config class.
    """
    
    def __init__(self):
        """
        Constructor for the Config class that initializes the ConfigParser.
        """
        super(Config, self).__init__()
