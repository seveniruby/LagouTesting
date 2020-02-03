
class Queue:
    def __init__(self):
        #todo: deque()
        self._data=[]

    def put(self, item):
        self._data.append()

    def get(self):
        result=self._data[0]
        self._data.remove(result)
        return result