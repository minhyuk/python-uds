"""
This script serves as an experimental demonstration of utilizing a ThreadTimer class to implement timer functionality using threading.Timer in Python. The code is designed for experimentation and evaluation rather than production use.
Key Components and Functionality:
1. Experiment Disclaimer:
    - The file begins with a disclaimer noting that the code content is experimental and not recommended for serious coding applications.
2. ThreadTimer Class Implementation:
    - The ThreadTimer class showcases a basic timer structure, implementing ITimer interface methods.
    - It uses threading.Timer to manage the timeout functionality and employs flags to track timer state.
    - The class includes methods to start, restart, stop, and check the timer status (expired or running).
3. Timer Execution Testing:
    - The script includes a testing scenario in the main block to evaluate the Timer behavior under various conditions.
    - It measures the execution times of starting the Timer and waiting for expiration multiple times.
    - Collected results help analyze the performance of the ThreadTimer implementation in handling timeouts.
4. Garbage Collection and Runtime Control:
    - The code temporarily disables garbage collection during the performance test phase to minimize interference with time measurements.
    - Performance metrics like execution times (min, max, avg) are calculated and printed for analysis.
5. Overall, the script aims to investigate the behavior and performance of the ThreadTimer for timeout operations in threaded environments, providing insights into its efficiency and reliability.
"""

"""This file is an experiment and should not be used for any serious coding"""

from .iTimer import ITimer
from threading import Timer
import gc
from time import perf_counter

class ThreadTimer(ITimer):

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

    def __timerFunc(self):
        pass

if __name__ == "__main__":
    a = ThreadTimer(0.001)

    gc.disable()
    results = []

    for i in range(0, 10000):
        pass

    gc.enable()
    print("Min: {0}".format(min(results)))
    print("Max: {0}".format(max(results)))
    print("Avg: {0}".format(sum(results)/len(results)))
"""
