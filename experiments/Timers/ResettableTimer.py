"""
This script defines a ResettableTimer class that extends the ITimer abstract base class for managing timer-related functionality in Python. The class offers features for time tracking, monitoring, and expiration-based actions, providing a flexible timer implementation in Python.
Key Components and Functionality:
1. Experiment Disclaimer:
    - The script opens with a disclaimer marking it as an experimental code snippet, indicating it is not intended for significant coding applications.
2. ResettableTimer Class:
    - ResettableTimer extends the ITimer abstract base class, inheriting the structure and requirements defined by ITimer.
    - The class features methods for timing functions such as starting, restarting, stopping, checking expiration status, and monitoring the running state of the timer.
3. Constructor and Attributes:
    - __init__(): Initializes the timer instance with a user-defined timeout value.
    - Attributes:
        - __timeout: Stores the timeout duration for the timer.
        - __active_flag: Tracks the active state of the timer.
        - __expired_flag: Indicates whether the timer has expired.
        - __startTime: Records the timestamp when the timer is started.
4. Method Details:
    - start(): Initiates the timer and resets the start time, active flag, and expired flag.
    - restart(): Calls the start method to restart the timer.
    - stop(): Disables the timer by setting the active flag to False.
    - isExpired(): Checks if the timer has expired based on the elapsed time compared to the timeout value.
    - isRunning(): Returns the current state of the timer - active or inactive.
5. The script proceeds to run the ResettableTimer for 10,000 iterations, measuring the performance with regards to the timer expiration times and calculating statistics like minimum, maximum, and average delta times.
6. This script provides a basic implementable blueprint for a resettable timer functionality, allowing users to track time intervals and manage timer-based actions efficiently.
"""

"""This file is an experiment and should not be used for any serious coding"""

from .iTimer import ITimer
from time import perf_counter
import gc

class ResettableTimer(ITimer):

    def __init__(self, timeout=0):

        self.__timeout = timeout

        self.__active_flag = False
        self.__expired_flag = False

        self.__startTime = 0

    def start(self):
        self.__startTime = perf_counter()
        self.__active_flag = True
        self.__expired_flag = False

    def restart(self):
        self.start()

    def stop(self):
        self.__active_flag = False

    def isExpired(self):
        if(self.__active_flag):
            if (perf_counter() - self.__startTime) > self.__timeout:
                self.__active_flag = False
                self.__expired_flag = True
                return self.__expired_flag
            else:
                return False
        return self.__expired_flag

    def isRunning(self):
        return self.__active_flag


if __name__ == "__main__":
    a = ResettableTimer(0.001)

    results = []
    for i in range(0, 10000):
        startTime = perf_counter()
        a.start()
        while (a.isExpired() == False):
            pass
        endTime = perf_counter()
        delta = endTime - startTime
        results.append(delta)

    print("Min: {0}".format(min(results)))
    print("Max: {0}".format(max(results)))
    print("Avg: {0}".format(sum(results)/len(results)))

"""
