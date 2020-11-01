"""
    @Difficulty : M
    @Status     : AC
    @Time       : 2020/10/25 10:54
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for p, q in zip(l, r):
            cut = sorted(nums[p: q+1])
            if len(cut) < 2:
                answer.append(False)
                continue

            diff = cut[1] - cut[0]
            flag = True
            for i in range(2, len(cut)):
                if cut[i] - cut[i-1] != diff:
                    flag = False
                    break
            answer.append(flag)

        return answer



if __name__ == '__main__':
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(Solution().checkArithmeticSubarrays(nums, l, r))

