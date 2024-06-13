#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import unittest
from uds import ResettableTimer
from time import sleep, perf_counter


class CanTpMessageTestCase(unittest.TestCase):

    ##
    # @brief tests the initialisation transition
    # Test method to verify the initial state of the ResettableTimer
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.6 seconds.
    # 2. Asserts that 'isRunning' method returns False, indicating the timer is not running initially.
    # 3. Asserts that 'isExpired' method returns False, indicating the timer is not expired initially.
    def testStateWhenInitialised(self):
            a = ResettableTimer(0.6)
            self.assertEqual(False, a.isRunning())
            self.assertEqual(False, a.isExpired())

    ##
    # @brief tests the state after starting
    # Test method to verify the state of the ResettableTimer after it is started
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.2 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Asserts that 'isRunning' method returns True, indicating the timer is running after being started.
    # 4. Asserts that 'isExpired' method returns False, indicating the timer is not expired immediately after being started.
    def testStateAfterStart(self):
            a = ResettableTimer(0.2)
            a.start()
            self.assertEqual(True, a.isRunning())
            self.assertEqual(False, a.isExpired())

    ##
    # @brief tests state after timeout
    # Test method to verify the state of the ResettableTimer after the timeout duration has elapsed
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.2 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Pauses execution for 0.25 seconds using sleep to allow the timer to expire.
    # 4. Asserts that 'isRunning' method returns False, indicating the timer is no longer running after the timeout.
    # 5. Asserts that 'isExpired' method returns True, indicating the timer has expired after the timeout duration has elapsed.
    def testStateAfterTimeoutTime(self):
            a = ResettableTimer(0.2)
            a.start()
            sleep(0.25)
            self.assertEqual(False, a.isRunning())
            self.assertEqual(True, a.isExpired())

    ##
    # @brief tests state after reset
    # Test method to verify the state of the ResettableTimer after it is restarted
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.4 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Pauses execution for 0.3 seconds using sleep.
    # 4. Restarts the timer by calling the 'restart' method.
    # 5. Pauses execution for another 0.2 seconds using sleep.
    # 6. Asserts that 'isRunning' method returns True, indicating the timer is running after being restarted.
    # 7. Asserts that 'isExpired' method returns False, indicating the timer is not expired shortly after being restarted.
    def testStateAfterRestart(self):
            a = ResettableTimer(0.4)
            a.start()
            sleep(0.3)
            a.restart()
            sleep(0.2)
            self.assertEqual(True, a.isRunning())
            self.assertEqual(False, a.isExpired())

    ##
    # @brief tests state for restart while running
    # Test method to verify the state of the ResettableTimer after it is restarted and then expires
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.4 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Pauses execution for 0.3 seconds using sleep.
    # 4. Asserts that 'isExpired' method returns False, indicating the timer has not expired yet.
    # 5. Asserts that 'isRunning' method returns True, indicating the timer is still running.
    # 6. Restarts the timer by calling the 'restart' method.
    # 7. Pauses execution for 0.45 seconds using sleep to allow the timer to expire.
    # 8. Asserts that 'isExpired' method returns True, indicating the timer has expired after the restart.
    # 9. Asserts that 'isRunning' method returns False, indicating the timer is no longer running after it has expired.
    def testStateAfterRestartAndExpiry(self):
            a = ResettableTimer(0.4)
            a.start()
            sleep(0.3)
            self.assertEqual(False, a.isExpired())
            self.assertEqual(True, a.isRunning())
            a.restart()
            sleep(0.45)
            self.assertEqual(True, a.isExpired())
            self.assertEqual(False, a.isRunning())

    ##
    # @brief tests state for restart after expiry
    # Test method to verify the state of the ResettableTimer after it has expired and then is restarted
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.4 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Pauses execution for 0.45 seconds using sleep to allow the timer to expire.
    # 4. Asserts that 'isRunning' method returns False, indicating the timer is no longer running after it has expired.
    # 5. Asserts that 'isExpired' method returns True, indicating the timer has expired.
    # 6. Restarts the timer by calling the 'restart' method.
    # 7. Asserts that 'isRunning' method returns True, indicating the timer is running again after being restarted.
    # 8. Asserts that 'isExpired' method returns False, indicating the timer is not expired immediately after being restarted.
    def testStateAfterExpiredThenRestart(self):
            a = ResettableTimer(0.4)
            a.start()
            sleep(0.45)
            self.assertEqual(False, a.isRunning())
            self.assertEqual(True, a.isExpired())
            a.restart()
            self.assertEqual(True, a.isRunning())
            self.assertEqual(False, a.isExpired())

    ##
    # @brief tests state after a stop
    # Test method to verify the state of the ResettableTimer after it is stopped following a start
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0.4 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Asserts that 'isRunning' method returns True, indicating the timer is running after being started.
    # 4. Asserts that 'isExpired' method returns False, indicating the timer is not expired immediately after being started.
    # 5. Stops the timer by calling the 'stop' method.
    # 6. Asserts that 'isRunning' method returns False, indicating the timer is not running after being stopped.
    # 7. Asserts that 'isExpired' method returns False, indicating the timer is not expired after being stopped.
    def testStopAfterStart(self):
            a = ResettableTimer(0.4)
            a.start()
            self.assertEqual(True, a.isRunning())
            self.assertEqual(False, a.isExpired())
            a.stop()
            self.assertEqual(False, a.isRunning())
            self.assertEqual(False, a.isExpired())

    ##
    # @brief tests state with a 0 timeout
    # Test method to verify the state of the ResettableTimer when initialized with a duration of 0 seconds
    # Args:
    #    self: The instance of the test case class.
    # 1. Creates an instance of ResettableTimer with a duration of 0 seconds.
    # 2. Starts the timer by calling the 'start' method.
    # 3. Asserts that 'isRunning' method returns False, indicating the timer is not running since the duration is 0.
    # 4. Asserts that 'isExpired' method returns True, indicating the timer is expired immediately upon being started.
    def testIsExpiredWith0Time(self):
            a = ResettableTimer(0)
            a.start()
            self.assertEqual(False, a.isRunning())
            self.assertEqual(True, a.isExpired())

    ##
    # @brief tests the accuracy of the timer
    # Test method to verify the accuracy of the ResettableTimer
    # Args:
    #    self: The instance of the test case class.
    # 1. Defines a list 'testTimes' with multiple durations to test the timer against.
    # 2. Iterates over each duration 'i' in 'testTimes':
    #    a. Creates an instance of ResettableTimer with the current duration 'i'.
    #    b. Records the start time using 'perf_counter'.
    #    c. Starts the timer by calling the 'start' method.
    #    d. Waits in a loop until the timer is no longer running.
    #    e. Records the end time using 'perf_counter'.
    #    f. Calculates the elapsed time 'delta' by subtracting 'startTime' from 'endTime'.
    #    g. Asserts that the elapsed time 'delta' is approximately equal to the duration 'i', within a tolerance of 0.001 seconds.
    def testTimerAccuracy(self):
            testTimes = [1, 0.3, 0.2, 0.1, 0.01, 0.01]
            for i in testTimes:
                a = ResettableTimer(i)
                startTime = perf_counter()
                a.start()
                while(a.isRunning()):
                    pass
                endTime = perf_counter()
                delta = endTime - startTime
                self.assertAlmostEqual(delta, i, delta=0.001)


if __name__ == "__main__":
    unittest.main()
