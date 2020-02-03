class LinkNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def append(self, data):
        tail = self
        while tail.next is not None:
            tail = tail.next
        tail.next = LinkNode(data)

    def travel(self):
        node = self
        while node is not None:
            print(node.data)
            node = node.next

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
            else:
                index += 1
                item = item.next

        node=LinkNode(data)
        node.next=item.next
        item.next=node


class TestLinkNode:
    def test_node(self):
        link = LinkNode(0)
        link.append(1)
        link.append(2)
        link.append(3)
        link.append(4)
        link.append(5)
        link.travel()
        link.insert(3, 'a')
        link.travel()
        print(link.search('a'))
