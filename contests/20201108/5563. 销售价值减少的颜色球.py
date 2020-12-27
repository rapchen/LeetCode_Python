"""
    @Difficulty : M 2
    @Status     : AC
    @Time       : 2020/11/8 10:52
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        inventory.append(0)

        res = 0
        for i in range(1, len(inventory)):
            if orders > (inventory[i-1] - inventory[i]) * i:
                orders -= (inventory[i-1] - inventory[i]) * i
            else:
                k = inventory[i-1] - orders // i
                remain = orders % i

                for j in range(i):
                    res = (res + (inventory[j] + k+1) * (inventory[j] - k) // 2) % 1000000007
                res = (res + k * remain) % 1000000007
                return res


if __name__ == '__main__':
    inventory = [2, 8, 4, 10, 6]
    orders = 20
    print(Solution().maxProfit(inventory, orders))

