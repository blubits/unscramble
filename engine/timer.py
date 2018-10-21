"""
Timer class for SWUG game engine.

:Author:     Jose Enrico Salinas
:Version:    v20181021
"""
from threading import Timer
import time

class GameTimer(Timer):
    
    def start(self):
        self.started_at = time.time()
        Timer.start(self)
    
    def elapsed(self):
        return time.time() - self.started_at
    
    def remaining(self):
        return self.interval - self.elapsed()