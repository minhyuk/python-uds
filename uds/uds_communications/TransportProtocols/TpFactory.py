
Attributes:
    configType (str): Config type.
    configParameters (list): List of configuration parameters.
    config (Config): Object to store the configuration.

Methods:
    __call__(tpType, configPath=None, **kwargs): Method to create different connection types based on the transport protocol.
    loadConfiguration(configPath=None): Loads the configuration parameters.

Raises:
    FileNotFoundError: If the specified config file is not found.
    NotImplementedError: If the specified transport protocol is not supported.
    Exception: If an unknown transport type is selected.
"""
