from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def get_size(self):
        return len(self._data)

    def get_depth(self, test_data):
        max_depth = 0
        for i in test_data:
            if i in "{[(":
                self.push(i)
                if max_depth < self.get_size():
                    max_depth = self.get_size()
            elif i in "}])":
                self.pop()
            else:
                pass
        return max_depth


class TestStack:
    def setup(self):
        self.stack = Stack()

    def test_d(self):
        test_data = "{xx{ddd{d{{{}}}ddd}dddd{x{[]}xx}dddd}}"
        print(self.stack.get_depth(test_data))

    def test_d2(self):
        test_data = "{xxx[xxx{xx[xxx]x}]xx{x[xxx]xxx{xxx}xx}x}"
        print(self.stack.get_depth(test_data))

    def test_queue(self):
        import queue
        queue.SimpleQueue


class Queue:
    def __init__(self):
        self._queue = deque()

    def put(self, item):
        self._queue.append(item)

    def get(self):
        return self._queue.popleft()
