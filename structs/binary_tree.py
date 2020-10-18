"""
    @Time    : 2020/9/29 14:20
    @Author  : Chen Runwen
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_values(values: list) -> "TreeNode":
        if not values:
            return None

        root = TreeNode(values[0])
        nodes = deque([root])

        for i in range(1, len(values), 2):
            if values[i] is not None:
                node = TreeNode(values[i])
                nodes.append(node)
                nodes[0].left = node

            if i + 1 < len(values) and values[i+1] is not None:
                node = TreeNode(values[i+1])
                nodes.append(node)
                nodes[0].right = node
            nodes.popleft()

        return root

    def to_values(self) -> list:
        res = []
        nodes = deque([self])

        while nodes:
            node = nodes.popleft()
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                nodes.append(node.left)
                nodes.append(node.right)

        while res[-1] is None:
            res.pop()
        return res

    def __str__(self) -> str:
        return str(self.to_values())




