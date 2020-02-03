class BTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def travel(self, subtree):
        if subtree is not None:
            self.travel(subtree.left)
            print(subtree.data)
            self.travel(subtree.right)

    def max_depth(self, subtree, depth):
        if subtree is None:
            return depth
        else:
            left_max=self.max_depth(subtree.left, depth + 1)
            right_max=self.max_depth(subtree.right, depth + 1)

            return left_max if left_max>right_max else right_max


class TestBTree:
    """
    0
    1 2
    3 4  | 5 6
    none none |  none none | none none |  7 none
    """

    def test_create(self):
        tree = BTree(0)
        tree.left = BTree(1)
        tree.right = BTree(2)
        tree.left.left = BTree(3)
        tree.left.right = BTree(4)
        tree.right.left = BTree(5)
        tree.right.right = BTree(6)
        tree.right.right.left=BTree(7)
        tree.travel(tree)

        print(tree.max_depth(tree, 0))
