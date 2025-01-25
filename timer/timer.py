import time
# optional class: depends on if we want to print the time to the player
class Timer:
    def __init__(self, countdown):
        self.count_until = countdown

    # starts the timer by logging the start time and the end time
    def begin(self):
      self.start = time.time()
      self.end = self.start + self.count_until

    # start at 2 <- subtract 32: -30
    # 3 <- 32-3 = -29
    # end at 32 (30 second timer) 32 = 0

    # returns a number representing how many seconds have passed in the timer
    # the timer is complete when check_time returns a number <= 0
    def check_time(self):
       current = time.time()
       return -(current - self.end)