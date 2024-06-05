"""
This Python script defines the ResettableTimer class, which implements timer functionality by inheriting from the ITimer abstract base class. The timer allows for setting a timeout threshold and tracking the elapsed time to determine if the timer has expired.

The ResettableTimer class includes the following methods:
1. __init__: Initializes the timer with a specified timeout value and sets internal flag variables to track the timer status.
2. start: Initiates the timer by recording the start time, setting the active flag, and resetting the expired flag.
3. restart: Restarts the timer by calling the start method.
4. stop: Stops the timer by deactivating the active flag.
5. isExpired: Checks if the timer has expired based on the timeout duration and updates the internal flags accordingly.
6. isRunning: Returns the current running status of the timer.

The script further includes a test block within the main condition that creates an instance of ResettableTimer, measures the time taken for multiple timer runs, and outputs statistical information such as the minimum, maximum, and average durations.

Overall, this script demonstrates the implementation of a resettable timer functionality with time tracking capabilities, providing a reusable and flexible timer component for time-based operations.
"""
