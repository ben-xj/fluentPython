import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = 0

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)