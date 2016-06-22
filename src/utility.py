import time


TIME_SPAN = 1.0


class FPSCounter(object):
    def __init__(self):
        super(FPSCounter, self).__init__()
        self._first = True
        self._fps = 0.0
        self._tick = 0
        self._last = time.time()

    def tick(self):
        self._tick += 1
        now = time.time()
        if now - self._last > TIME_SPAN:
            self._first = False
            self._fps = self._tick / TIME_SPAN
            self._tick = 0
            self._last = now

    def get_fps(self):
        if self._first:
            return "Counting..."
        else:
            return self._fps
