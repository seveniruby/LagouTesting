from test_struct.test_stack import Stack


class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def travel(self, node=None, depth=1):
        # 第一步递归改造
        # 第二步改造增加默认参数
        # 第三步改造增加depth
        # 第四步改造使用生成器
        if node is None:
            node = self
        yield node.data, depth
        depth += 1
        for child in node.children:
            yield from self.travel(child, depth)
        depth -= 1

    @staticmethod
    def create_from_string(content) -> 'Tree':
        #第一步编写基本的字符串处理逻辑框架
        #第二步创建节点
        #第三步使用stack记录tree的当前节点
        key=""
        root:Tree=None
        stack=Stack()
        for c in content:
            if c is "<":
                key=""
            elif c is ">":
                if "/" in key:
                    #节点结束
                    stack.pop()
                else:
                    #新节点
                    tree=Tree(key)
                    if root is None:
                        root=tree
                    else:
                        stack.top().children.append(tree)
                    stack.push(tree)
            else:
                key+=c
        return root



class TestTree:
    def test_create_tree(self):
        root = Tree("html")
        head = Tree("head")
        a = Tree("a")
        b = Tree("b")
        head.children.append(a)
        head.children.append(b)
        body = Tree("body")
        x = Tree("x")
        m = Tree("m")
        m.children.append(x)
        body.children.append(m)
        root.children.append(head)
        root.children.append(body)
        print()
        tree_dict = {}
        for node, depth in root.travel():
            print(f"{'  ' * depth}{node} depth={depth}")
            tree_dict[node] = depth

        assert tree_dict["x"] == 4
        assert tree_dict["b"] == 3
        assert tree_dict["body"] == 2
        assert tree_dict["html"] == 1

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
        print()
        for data, depth in root.travel():
            tree_dict[data] = depth
            print(f"{'  ' * depth}{data} depth={depth}")
        assert tree_dict["html"] == 1
        assert tree_dict["head"] == 2
        assert tree_dict["body"] == 2
        assert tree_dict["d"] == 3
        assert tree_dict["m"] == 3
        assert tree_dict["x"] == 4
