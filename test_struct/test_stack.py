class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def get_size(self):
        return len(self._data)

    def top(self):
        if self._data:
            return self._data[-1]
        else:
            return ''

    def pattern(self, content: str) -> bool:
        for c in content:
            if self.top() + c in ['[]', '{}', '()']:
                self.pop()
            else:
                self.push(c)
        return self.get_size() == 0

    def travel(self):
        return self._data


class TestStack:
    def setup(self):
        self.stack = Stack()

    def test_demo(self):
        self.stack.push(3)
        self.stack.push(2)
        self.stack.push(1)
        assert self.stack.pop() == 1
        assert self.stack.pop() == 2
        assert self.stack.pop() == 3

    def match(self, data):
        for c in data:
            if c in "{[(":
                self.stack.push(c)
            elif c in ")]}":
                self.stack.pop()
        return self.stack.get_size() == 0

    def test_match(self):
        test_data = "{xxxxx[dddddddd(xxxxx{ddddd}dfsfe)dfsefe]xxxx}"
        assert self.match(test_data) == True

        test_data = "{xxxx[ddddd]xxxx"
        assert self.match(test_data) == False

    def test_pattern(self):
        assert self.stack.pattern("[]") == True
        assert self.stack.pattern("[{}]") == True
        assert self.stack.pattern("[{()}]") == True
        assert self.stack.pattern("[") == False
        assert self.stack.pattern("[{]}") == False
        assert self.stack.pattern("[{(})]") == False
