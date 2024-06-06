
"""
This script defines an abstract base class ITimer using the abc module to establish a Time Interface for timer functionality in Python. The class outlines abstract methods required for timer management, offering a standardized structure for timer implementations.
Key Components and Functionality:
1. Experiment Disclaimer:
    - The code snippet commences with a note highlighting it as an experimental file, advising against using it for significant coding purposes.
2. ITimer Abstract Base Class Definition:
    - ITimer class serves as an abstract base class outlining a timer interface through abstract methods, present in abstract base classes (ABC).
    - The class incorporates abstract methods for starting, restarting, stopping, checking expiration status, and monitoring the running state of a timer.
3. Method Signatures:
    - start(): Abstract method signature for commencing a timer.
    - restart(): Abstract method signature for restarting a timer.
    - stop(): Abstract method signature for stopping or canceling a timer.
    - isExpired(): Abstract method signature for determining if a timer has expired.
    - isRunning(): Abstract method signature for checking the running status of a timer.
4. Overall, this script sets the foundation for defining timer-related interfaces and behaviors, offering a clear structure for derived timer classes leveraging the ITimer interface.
"""

"""This file is an experiment and should not be used for any serious coding"""

import abc


class ITimer(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def restart(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def isExpired(self):
        pass

    @abc.abstractmethod
    def isRunning(self):
        pass

