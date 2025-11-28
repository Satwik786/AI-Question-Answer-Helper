from collections import deque

class ShortTermMemory:
    def __init__(self, size=3):
        self.buffer = deque(maxlen=size)

    def add(self, message):
        self.buffer.append(message)

    def get_context(self):
        return list(self.buffer)
