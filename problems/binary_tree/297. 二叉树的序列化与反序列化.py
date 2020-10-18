"""
    @Difficulty : H
    @Status     : AC 99% 50%
    @Time       : 2020/10/15 23:18
    @Author     : Chen Runwen
"""
from collections import deque

from structs.binary_tree import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = []
        nodes = deque([root])

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
        return ','.join([str(v) for v in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        values = [None if v == 'None' else int(v) for v in data.split(',')]

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


if __name__ == '__main__':
    tree = TreeNode.from_values([1,2,3,None,None,4,5])
    s = Codec().serialize(tree)
    tree1 = Codec().deserialize(s)
    print(tree1)

