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
