"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/10/25 10:29
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(keysPressed)
        max_time = releaseTimes[0]
        res = keysPressed[0]

        for i in range(n):
            t = releaseTimes[i] - releaseTimes[i-1]
            if t > max_time or (t == max_time and keysPressed[i] > res):
                max_time, res = t, keysPressed[i]

        return res


if __name__ == '__main__':
    releaseTimes = [12,23,36,46,62]
    keysPressed = "spuda"
    print(Solution().slowestKey(releaseTimes, keysPressed))

