from test_struct.test_stack import Stack


class BTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        # self.children=[]

    def travel_subtree(self, subtree):
        if subtree is None:
            return

        self.travel_subtree(subtree.left)
        print(subtree.data)
        self.travel_subtree(subtree.right)

    def travel(self):
        return self.travel_subtree(self)

    def max_depth(self, subtree, depth):
        if subtree is None:
            return depth

        max_left = self.max_depth(subtree.left, depth + 1)
        max_right = self.max_depth(subtree.right, depth + 1)
        return max_left if max_left > max_right else max_right

    def get_max_depth(self):
        return self.max_depth(self, 0)


class TestBTee:
    """
    0
    1 2
    3 4 | 5 6
    none none | none none | none none | 7 none
    """

    def setup(self):
        self.tree = BTree(0)
        self.tree.left = BTree(1)
        self.tree.right = BTree(2)
        self.tree.left.left = BTree(3)
        self.tree.left.right = BTree(4)
        self.tree.right.left = BTree(5)
        self.tree.right.right = BTree(6)
        self.tree.right.right.left = BTree(7)

    def test_travel(self):
        self.tree.travel()

    def test_max_depth(self):
        assert self.tree.max_depth(self.tree, 0) == 4
        self.tree.right.right.left.left = BTree(8)
        assert self.tree.max_depth(self.tree, 0) == 5
        assert self.tree.get_max_depth() == 5


class Tree:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def travel(self, current=None, depth=1):
        if current is None:
            current = self
        yield current, depth

        depth += 1
        for child in current.children:
            yield from self.travel(child, depth)
        depth -= 1

    def create(self, content: str):
        stack = Stack()
        key = ""
        current = None
        parent = None
        root = self

        for c in content:
            if c is "<":
                key = ""
            elif c is ">":

                if "/" in key:
                    stack.pop()
                    current = stack.top()
                else:
                    sub_tree = Tree(key)
                    if current:
                        current.children.append(sub_tree)
                    else:
                        root = sub_tree
                    current = sub_tree
                    stack.push(current)
            else:
                key += c

        return root

    def path(self, data):
        stack = Stack()
        for sub_tree, depth in self.travel():
            while depth <= stack.get_size():
                stack.pop()
            stack.push(sub_tree)

            if data == sub_tree.data:
                return "".join([item.data for item in stack.travel()])


class TestTree:
    def test_travel_new(self):
        tree = Tree("a")
        tree.children.append(Tree("b"))
        tree.children.append(Tree("c"))
        print()
        for item, depth in tree.travel():
            print(f"{'  ' * depth} {item.data}")

    def test_path(self):
        xml = """
        <a>
          <b>
            <c></c>
            <d></d>
          </b>
          <f>
            <e></e>
          </f>
          <m><n><x><y></y></x></n></m>
        </a>
        """

        tree = Tree()
        tree = tree.create(xml)
        print([f"{item.data} {depth}" for item, depth in tree.travel()])

        assert tree.path("a") == "a"
        assert tree.path("b") == "ab"
        assert tree.path("d") == "abd"
        assert tree.path("y") == "amnxy"
