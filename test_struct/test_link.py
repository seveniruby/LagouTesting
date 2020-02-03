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
            yield item
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

    def order(self, data):
        pre = self
        for item in self.travel():
            if data < item.data:
                break
            pre = item

        node_new = LinkNode(data)
        node_new.next = pre.next
        pre.next = node_new

        return self


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

    def test_order(self):
        self.link = LinkNode(1)
        self.link.order(5).order(3).order(2).order(4)
        link_data = [item.data for item in self.link.travel()]
        print(link_data)
        assert link_data == [1, 2, 3, 4, 5]

        self.link.append(7).append(6)
        link_data = [item.data for item in self.link.travel()]
        print(link_data)
        assert link_data != sorted(link_data)

