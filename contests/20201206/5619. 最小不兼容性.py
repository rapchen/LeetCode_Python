"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2020/12/6 10:26
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    """ 动规 """
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        self.nums = nums
        n = len(nums)
        self.k = k
        np = n // k

        # dp[t]: 当前可用数字索引
        self.dp = [1000000] * (2 ** n)
        self.dp[-1] = 0
        for i in range(k):
            self.new = [1000000] * (2 ** n)
            for self.t in range(2 ** n):
                if self.dp[self.t] > 100000:
                    continue
                # 遍历下一组的所有可能情况（递归）
                self.used = []
                self.usable = set()
                for j in range(n):
                    if self.t & (1 << j) > 0:
                        if not self.used:
                            self.used.append(j)
                        else:
                            self.usable.add(j)
                self.dfs(np - 1)
            self.dp = self.new

        return self.dp[0] if self.dp[0] < 100000 else -1


    def dfs(self, remain):
        """ 用回溯遍历remain个数的所有可能组合 """
        used_nums = [self.nums[j] for j in self.used]
        if remain == 0:
            new_t = sum([1 << j for j in self.usable])
            addition = max(used_nums) - min(used_nums)
            self.new[new_t] = min(self.new[new_t], self.dp[self.t] + addition)
            return

        for j in self.usable:
            if j < self.used[-1] or self.nums[j] in used_nums:
                continue
            self.used.append(j)
            self.usable.remove(j)

            self.dfs(remain - 1)

            self.usable.add(j)
            self.used.pop()




if __name__ == '__main__':
    # nums = [1, 2, 1, 4]
    # k = 2
    # nums = [6, 3, 8, 1, 3, 1, 2, 2]
    # k = 4
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    k = 8
    print(Solution().minimumIncompatibility(nums, k))

