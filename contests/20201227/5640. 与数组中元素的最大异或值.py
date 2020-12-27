"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/12/27 10:29
    @Author     : Chen Runwen
"""
from typing import List


class TreeNode:
    def __init__(self, val):
        self.min = val  # 这颗子树里最小的数
        self.b0 = None
        self.b1 = None


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 构建二叉树
        root = TreeNode(min(nums))
        for k in nums:
            b = bin(k)[2:]
            b = '0' * (30 - len(b)) + b
            node = root
            for bit in b:
                if bit == '0':
                    if not node.b0:
                        node.b0 = TreeNode(k)
                    node = node.b0
                else:
                    if not node.b1:
                        node.b1 = TreeNode(k)
                    node = node.b1
                node.min = min(node.min, k)

        # 开始查找
        ans = []
        for x, m in queries:
            if m < root.min:
                ans.append(-1)
                continue

            b = bin(x)[2:]
            b = '0' * (30 - len(b)) + b
            node = root
            for bit in b:
                if bit == '0':
                    if node.b1 and node.b1.min <= m:
                        node = node.b1
                    else:
                        node = node.b0
                else:
                    if node.b0 and node.b0.min <= m:
                        node = node.b0
                    else:
                        node = node.b1
            ans.append(x ^ node.min)
        return ans


if __name__ == '__main__':
    print(Solution())

