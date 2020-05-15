class RingBuffer:
    def __init__(self, capacity):
        self.container = []
        self.capacity = capacity
        self.index = 0

    def append(self, item):
        if len(self.container) == self.capacity:
            self.container.pop(self.index)
            self.container.insert(self.index, item)
            self.index += 1
            if self.index >= self.capacity:
                self.index = 0
        else:
            self.container.append(item)

    def get(self):
        return self.container