class Random:
    def __init__(self, seed=None):
        if seed is None:
            seed = id(object())

        self.seed = seed & 0xFFFFFFFF

    def next(self):
        self.seed = (self.seed * 1664525 + 1013904223) & 0xFFFFFFFF
        x = self.seed

        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17)
        x ^= (x << 5) & 0xFFFFFFFF

        return x & 0xFFFFFFFF

    def randint(self, a, b):
        return a + (self.next() % (b - a + 1))