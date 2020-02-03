import pprint


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
        if self.get_size() == 0:
            return None
        else:
            return self._data[-1]

    def pattern(self, str: str) -> bool:
        for c in str:
            if f"{self.top()}{c}" in ["[]", "{}", "()"]:
                self.pop()
            else:
                self.push(c)
            print(self._data)
        return self.get_size() == 0

    def travel(self):
        return self._data


class TestStack:
    def setup(self):
        self.stack = Stack()

    def test_pattern(self):
        assert self.stack.pattern("()") == True
        assert self.stack.pattern("([])") == True
        assert self.stack.pattern("([{[]}{}])") == True
        assert self.stack.pattern("([)") == False
        assert self.stack.pattern("([{[]}{{}])") == False
        assert self.stack.pattern("([{[]}{]})") == False


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
        item = self.next
        while item is not None:
            print(item.data)
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
        for i in self.travel():
            if data < i.data:
                break
            else:
                pre = i

        node_new = LinkNode(data)
        node_new.next = pre.next
        pre.next = node_new
        return self


class TestLink:
    def setup(self):
        self.link_1 = LinkNode()
        self.link_1.append(1).append(5).append(3).append(2).append(4)

        self.link_2 = LinkNode()
        self.link_2.append(1).append(2).append(3).append(4).append(5)

        self.link_3 = LinkNode()
        self.link_3.append(1).append(2).append(3).append(4).append(5)

    def test_link_sort(self):
        self.link = LinkNode()
        self.link.order(1).order(5).order(3).order(2).order(4)
        list_data = [i.data for i in self.link.travel()]
        print(list_data)
        assert list_data == sorted(list_data)

        self.link.append(1)
        list_data = [i.data for i in self.link.travel()]
        print(list_data)
        assert list_data != sorted(list_data)


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def travel(self, current=None, depth=0):
        if current is None:
            current = self
            depth = 1
        yield current, depth
        depth += 1
        for child in current.children:
            yield from self.travel(child, depth)
        depth -= 1

    @classmethod
    def create(cls, xml):
        parents = Stack()
        current, root = None, None
        key = ""
        for c in xml:
            if c == "<":
                key = ""
            elif c == ">":
                if "/" in key:
                    parents.pop()
                    current = parents.top()
                elif len(key) > 0:
                    tree_new = Tree(key)
                    if current:
                        current.children.append(tree_new)
                    else:
                        root = tree_new
                    current = tree_new

                    parents.push(current)
            else:
                key += c
        return root

    def path(self, data):
        stack = Stack()
        for sub_tree, depth in self.travel():
            while stack.get_size() > depth - 1:
                stack.pop()
            stack.push(sub_tree.data)

            if sub_tree.data == data:
                return "".join([str(item) for item in stack.travel()])


class TestTree:
    def test_path(self):
        xml = """<a>
          <b>
            <c></c>
            <d></d>
          </b>
          <e>
            <f></f>
          </e>
          <m><n><x><y></y></x></n></m>
        </a>"""
        self.tree = Tree.create(xml)
        assert self.tree.path("d") == "abd"
        assert self.tree.path("f") == "aef"
        assert self.tree.path("e") == "ae"
        assert self.tree.path("a") == "a"
        assert self.tree.path("y") == "amnxy"
