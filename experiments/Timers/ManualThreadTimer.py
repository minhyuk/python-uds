"""
This script is an experimental demonstration presenting a ManualThreadTimer implementation using threading.Thread in Python for the timer functionality. The code structure focuses on investigating the behavior and performance of a manual timer operation.
Key Components and Functionality:
1. Experiment Disclaimer:
    - The script begins with a disclaimer highlighting it as an experimental file and advises against using it for critical coding purposes.
2. ManualThreadTimer Class Definition:
    - The ManualThreadTimer class defines a manual thread-based timer for handling timeouts based on the ITimer interface.
    - It utilizes threading.Thread for the timer functionality and features methods to start, restart, stop, and check timer status.
    - The class maintains flags to monitor the active and expired states of the timer.
3. Timer Execution Logic:
    - The timerFunc method specifies the behavior of the timer thread, setting active and expired flags based on the timeout duration.
    - The start method initiates the timer thread, while the stop method is a placeholder for potential timer termination functionality.
4. ManualThreadTimer Testing:
    - The script conducts a performance test in the main block to evaluate the behavior of the ManualThreadTimer under various conditions.
    - Multiple timer start-stop cycles are measured to collect execution time data for analysis.
5. Results and Metrics:
    - The code calculates and outputs statistics such as minimum, maximum, and average timer durations observed during the performance test.
6. Overall, this file serves as an experimental platform for studying manual thread-based timer implementations and analyzing their efficacy in managing timeouts.
"""

"""This file is an experiment and should not be used for any serious coding"""

from .iTimer import ITimer
from threading import Thread
from time import perf_counter

class ManualThreadTimer(ITimer):

    def __init__(self, timeout=0):
        pass

    def start(self):
        pass

    def restart(self):
        self.start()

    def stop(self):
        pass

    def isExpired(self):
        pass

    def isRunning(self):
        pass

    def threadFunc(self):
        pass

if __name__ == "__main__":
    a = ManualThreadTimer(0.001)

    results = []
    for i in range(0, 10000):
        pass

    print("Min: {0}".format(min(results)))
    print("Max: {0}".format(max(results)))
    print("Avg: {0}".format(sum(results) / len(results)))
"""
