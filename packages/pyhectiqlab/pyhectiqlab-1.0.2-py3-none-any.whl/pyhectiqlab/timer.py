import threading

class RepeatedTimer(threading.Thread):
    def __init__(self, event, method, delay):
        super().__init__()
        self.daemon = True
        self.stopped = event
        self.delay = delay
        self.method = method

    def run(self):
        while not self.stopped.wait(self.delay):
            self.method()