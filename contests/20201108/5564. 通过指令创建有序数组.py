"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/11/8 11:09
    @Author     : Chen Runwen
"""
from typing import List


class TreeNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.count = 1  # 当前节点相同数的个数
        self.total = 1  # 子树的总数
        self.left = None
        self.right = None


class BST:

    def __init__(self, val) -> None:
        self.root = TreeNode(val)

    @staticmethod
    def total(node: TreeNode):
        return 0 if not node else node.total

    def insert(self, val):
        self.root, small, big = self._insert(val, self.root)
        return small, big

    def _insert(self, val, node):
        if node is None:
            return TreeNode(val), 0, 0

        if node.val == val:
            node.count += 1
            small = self.total(node.left)
            big = self.total(node.right)
        elif node.val > val:
            node.left, small, big = self._insert(val, node.left)
            big += node.count + self.total(node.right)
        else:
            node.right, small, big = self._insert(val, node.right)
            small += node.count + self.total(node.left)
        node.total += 1
        return node, small, big


class TreeArray:

    def __init__(self, size) -> None:
        self.size = size
        self.a = [0] * size

    def add1(self, idx):
        self.a[idx] += 1
        i = 1
        while i <= self.size:
            if idx & i == 0:
                idx = idx | i
                if idx >= self.size:
                    break
                self.a[idx] += 1
            i <<= 1

    def sum_head(self, idx):
        """ 比idx小的那些求和 """
        if idx == 0:
            return 0
        sum = 0
        while idx > 0:
            sum += self.a[idx - 1]
            idx = idx & (idx - 1)
        return sum

    def sum_tail(self, idx):
        if idx == self.size - 1:
            return 0
        return self.sum_head(self.size) - self.sum_head(idx + 1)


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = list(set(instructions))
        nums.sort()
        idx = {nums[i]: i for i in range(len(nums))}


        tree = TreeArray(len(nums))
        res = 0
        for n in instructions:
            i = idx[n]
            tree.add1(i)
            small = tree.sum_head(i)
            big = tree.sum_tail(i)
            res += min(small, big)

        return res % 1000000007



if __name__ == '__main__':
    instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]
    # instructions = [1,2,3,6,5,4]
    print(Solution().createSortedArray(instructions))

