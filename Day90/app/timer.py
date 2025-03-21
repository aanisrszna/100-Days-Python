import threading

class WritingTimer:
    def __init__(self, callback, timeout=5):
        self.timeout = timeout
        self.callback = callback
        self.timer = None

    def start_timer(self):
        """Starts or resets the countdown timer"""
        self.stop_timer()
        self.timer = threading.Timer(self.timeout, self.callback)
        self.timer.start()

    def stop_timer(self):
        """Stops the timer if running"""
        if self.timer:
            self.timer.cancel()
