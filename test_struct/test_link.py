class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data=None):
        item = self
        while item.next is not None:
            item = item.next

        item.next = LinkNode(data)
        return self

    def travel(self):
        item = self
        while item is not None:
            print(item.data)
            item = item.next

    def search(self, data):
        item = self
        index = 0
        while item is not None:
            if item.data == data:
                return index
            else:
                index += 1
                item = item.next
        return -1

    def insert(self, pos, data):
        item = self
        index = 0
        while item is not None:
            if index == (pos - 1):
                break
            index += 1
            item = item.next

        node = LinkNode(data)
        node.next = item.next
        item.next = node


class TestLinkNode:
    def setup(self):
        self.link = LinkNode(0)
        self.link.append(1)
        self.link.append(2).append(3).append(4).append(5)
        self.link.travel()

    def test_add(self):
        link = LinkNode(0)
        link.next = LinkNode(1)
        link.next.next = LinkNode(2)

    def test_append(self):
        link = LinkNode(0)
        link.append(1)
        link.append(2).append(3).append(4).append(5)
        link.travel()

    def test_search(self):
        print(self.link.search(3))
        print(self.link.search(0))

    def test_insert(self):
        self.link.insert(3, 2.5)
        self.link.travel()
        print(self.link.search(2.5))
