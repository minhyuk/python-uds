"""
This script is an experimental implementation that demonstrates the usage of multiprocessing in Python to create a timer functionality using shared memory Value objects. The main purpose of the code is to test the performance of the timer mechanism under different conditions.
Key Components and Functionality:
1. Experiment Disclaimer:
    - The file starts with a disclaimer warning stating that the content within is experimental and not intended for serious coding purposes.
2. Main Functionality:
    - The script defines a timer function and a MultiprocessingThread class implementing ITimer interface.
    - The timer function 'timerFunc' monitors the active_flag and calculates the elapsed time to check for timeouts.
    - The MultiprocessingThread class uses multiprocessing to manage the timer, with methods to start, restart, stop, and check the timer status.
3. Timer Testing:
    - The script includes a test scenario within the main block to test the timer behavior under heavy load.
    - It starts multiple timer instances, records the execution times, and analyzes the results.
    - The script prints out minimum, maximum, and average execution times, as well as indices with execution times under a threshold.
4. Multiprocessing and Performance Testing:
    - The code aims to evaluate the efficiency and accuracy of the implemented timer using the multiprocessing module.
    - Performance metrics such as execution times and timer accuracy are collected and analyzed for assessment.
5. Runtime Control:
    - The script runs multiple iterations of the timer test and provides an analysis of collected data.
6. Overall, the script serves as an experimental playground to test and evaluate the timer functionality under varying workloads and conditions.
"""

"""This file is an experiment and should not be used for any serious coding"""

from multiprocessing import Process, Value
from .iTimer import ITimer
from time import perf_counter, sleep

def timerFunc(active_flag, expired_flag, timeout):
    pass

class MultiprocessingThread(ITimer):

    def __init__(self, timeout):
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

if __name__ == "__main__":
    a = MultiprocessingThread(0.001)
    sleep(0.1)

    results = []

    for i in range(0, 10000):
        pass

    print("Min: {0}".format(min(results)))
    print("Max: {0}".format(max(results)))
    print("Avg: {0}".format(sum(results)/len(results))

    for i in range(0, len(results)):
        if results[i] < 0.001:
            print(i, results[i])

    sleep(50)
"""
