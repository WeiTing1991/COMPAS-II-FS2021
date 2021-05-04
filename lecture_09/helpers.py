from __future__ import print_function
import time


class Rate(object):
    def __init__(self, hz):
        self.hz = hz
        self.last_time = time.time_ns()
        self.sleep_duration = int(1e9 / hz)

    def sleep(self):
        t1 = time.time_ns()
        elapsed = t1 - self.last_time
        sleep_ns = (self.sleep_duration - elapsed)
        if sleep_ns > 0:
            time.sleep(sleep_ns / 1e9)
        self.last_time = self.last_time + self.sleep_duration
