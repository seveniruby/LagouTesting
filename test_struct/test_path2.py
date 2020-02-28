from test_struct.test_stack import Stack


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def travel(self, node=None, depth=1):
        if node is None:
            node = self
        yield node.data, depth
        depth += 1
        for child in node.children:
            yield from self.travel(child, depth)
        depth -= 1

    @staticmethod
    def create_from_string(content):
        key = ""
        stack = Stack()
        root: Tree = None

        for c in content:
            if "<" == c:
                key = ""
            elif ">" == c:
                if '/' in key:
                    stack.pop()
                else:
                    tree = Tree(key)
                    if root is None:
                        root = tree
                    else:
                        stack.top().children.append(tree)
                    stack.push(tree)
            else:
                key += c
        return root


class TestTree:
    def test_create_tree(self):
        root = Tree(1)
        tree2 = Tree(2)
        tree2.children.append(Tree(4))
        tree2.children.append(Tree(5))
        tree3 = Tree(3)
        tree3.children.append(Tree(6))
        tree3.children.append(Tree(7))

        root.children.append(tree2)
        root.children.append(tree3)
        print()
        for data, depth in root.travel():
            print(f'{"    " * (depth - 1)}data={data} depth={depth}')

    def test_create_tree_from_string(self):
        xml = """
        <html>
            <head>
                <c></c>
                <d></d>
            </head>
            <body>
                <m>
                    <x></x>
                </m>
            </body>
        </html>
        """

        root = Tree.create_from_string(xml)
        tree_dict = {}
        for data, depth in root.travel():
            tree_dict[data] = depth
        assert tree_dict["html"] == 1
        assert tree_dict["head"] == 2
        assert tree_dict["body"] == 2
        assert tree_dict["d"] == 3
        assert tree_dict["m"] == 3
        assert tree_dict["x"] == 4
