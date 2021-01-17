"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2021/1/10 10:25
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        for k in encoded:
            ans.append(ans[-1] ^ k)
        return ans

if __name__ == '__main__':
    print(Solution())
