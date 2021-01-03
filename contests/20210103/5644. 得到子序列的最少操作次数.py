"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/1/3 10:16
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    """ 类似最长递增子序列长度的做法 """
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # pos: 记录target中每个数出现位置
        pos = {target[i]: i for i in range(len(target))}
        # dp[i]: 记录以target中第i项为结尾的最长子序列长度
        # imax[i]: 记录dp中第一个值为i的下标
        imax = [-1]

        # 最长公共子序列
        for num in arr:
            if num not in pos:
                continue
            p = pos[num]
            # 二分查找在imax中的位置
            lo, hi = 0, len(imax)
            while hi - lo > 1:
                mid = (lo + hi) // 2
                if p <= imax[mid]:
                    hi = mid
                else:
                    lo = mid
            # 更新lo+1位置
            if lo == len(imax) - 1:
                imax.append(p)
            else:
                imax[lo + 1] = p

        # 次数
        maxlen = len(imax) - 1
        return len(target) - maxlen


if __name__ == '__main__':
    print(Solution())
