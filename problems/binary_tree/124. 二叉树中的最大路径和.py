"""
    @Difficulty : H
    @Status     : AC 91% 82%
    @Time       : 2020/10/15 22:52
    @Author     : Chen Runwen
"""
from structs.binary_tree import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return self.dfs(root)[0]

    def dfs(self, node) -> tuple:
        """ 深搜，返回以该节点为根节点的子树的最大路径；还有以该节点为一端的往下的最大路径 """
        if not node:
            return float('-inf'), 0
        max_l, max_single_l = self.dfs(node.left)
        max_r, max_single_r = self.dfs(node.right)
        max_single_ = max(node.val + max(max_single_l, max_single_r), 0)
        max_ = max(max_l, max_r, node.val + max_single_l + max_single_r)
        return max_, max_single_


if __name__ == '__main__':
    print(Solution())

