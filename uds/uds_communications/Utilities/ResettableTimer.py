"""
This class implements a resettable timer that starts counting time when it is initiated.

Attributes:
- timeoutTime (int): The duration in seconds for the timer.
- active_flag (bool): Flag to track if the timer is active.
- expired_flag (bool): Flag to indicate if the timer has expired.
- startTime (float): The starting time when the timer is initiated.

Methods:
- start(): Starts the timer by setting active_flag, startTime, and resetting expired_flag.
- restart(): Restarts the timer by calling the start method.
- stop(): Stops the timer by setting active_flag and expired_flag to False.
- isRunning(): Checks if the timer is currently running and updates expired_flag.
- isExpired(): Checks if the timer has expired and updates expired_flag if necessary.
- timerCheck(): Internal method to check the timer status.

This class implements the iResettableTimer interface and provides functionality to control and check the timer status.
"""
