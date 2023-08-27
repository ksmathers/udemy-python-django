class Calc:
    def __init__(self):
        self.clear()

    def add(self, v):
        self._acc += v

    def accum(self):
        return self._acc

    def clear(self):
        self._acc = 0
