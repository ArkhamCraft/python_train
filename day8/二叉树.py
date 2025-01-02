# 二叉树的建树，前序，中序，后序，层序遍历
from collections import deque


class Node(object):
    def __init__(self, elem=-1, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.myQueue = []

    def build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.myQueue.append(node)
        else:
            self.myQueue.append(node)
            if self.myQueue[0].left is not None:
                self.myQueue[0].left = node
            else:
                self.myQueue[0].right = node
                self.myQueue.pop(0)

    def pre_order(self, node: Node):
        if node:
            print(node.elem,end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)


    def in_order(self, node: Node):
        if node:
            self.in_order(node.left)
            print(node.elem,end=' ')
            self.in_order(node.right)

    def post_order(self, node: Node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.elem,end=' ')

    def breadth_first(self):
        help_queue = []
        help_queue.append(self.root)
        while help_queue:
            out_node = help_queue.pop(0)
            print(out_node.elem,end=' ')
            if out_node.left:
                help_queue.append(out_node.left)
            if out_node.right:
                help_queue.append(out_node.right)

tree = BinaryTree()
for i in range(1,11):
    new_node = Node(i)
    tree.build_tree(new_node)
tree.pre_order(tree.root)
print()
tree.in_order(tree.root)
print()
tree.post_order(tree.root)
print()
tree.breadth_first()
