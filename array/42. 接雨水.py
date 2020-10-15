"""
    @Time    : 
    @Author  : Chen Runwen
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l <= 2:
            return 0
        i = 0
        j = 1
        sum = 0
        while j < l:
            while j < l and height[j] < height[i]:
                j += 1
            if j == l:
                # 说明现在的height[i]是最高的
                j -= 1
                while j > i:
                    wall = height[j]
                    while j > i and height[j] <= wall:
                        sum += wall - height[j]
                        j -= 1
                return sum

            # height[j] 比 height[i] 高
            wall = height[i]
            while i < j:
                sum += wall - height[i]
                i += 1
            j += 1
        return sum



if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
