"""
    @Difficulty : H
    @Status     : TODO
    @Time       : 2020/10/25 11:02
    @Author     : Chen Runwen
"""
from typing import List


class Solution:
    """ 先排序，从小到大依次填写，每次填完更新对应行列下一个应该填的值 TODO 要用并查集 """

    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[0] * n for i in range(m)]
        # row: 代表这一行上次填的值
        row = [0 for i in range(m)]
        col = [0 for j in range(n)]

        nums = [(matrix[i][j], i, j) for i in range(m) for j in range(n)]
        nums.sort(key=lambda x: x[0])

        for idx, r in enumerate(nums):
            num, i, j = r
            if ans[i][j] != 0:
                continue
            # 找到所有跟当前格子应该相同的格子
            grids = {(i, j)}
            ii = {i}
            jj = {j}
            for k in range(idx + 1, m * n):
                if nums[k][0] != num:
                    break
                if nums[k][1] in ii or nums[k][2] in jj:
                    ii.add(nums[k][1])
                    jj.add(nums[k][2])
                    grids.add((nums[k][1], nums[k][2]))

            res = 0
            for i1, j1 in grids:
                res = max(res, row[i1] + 1, col[j1] + 1)

            for i1, j1 in grids:
                ans[i1][j1] = res
                row[i1] = col[j1] = res
                if ta[i1][j1] != res:
                    print("错了！", i1, j1, res, ta[i1][j1])

        return ans


if __name__ == '__main__':
    matrix = [[-24,-9,-14,-15,44,31,-46,5,20,-5,34],[9,-40,-49,-50,17,40,35,30,-39,36,-49],[-18,-43,-40,-5,-30,9,-28,-41,-6,-47,12],[11,42,-23,20,35,34,-39,-16,27,34,-15],[32,27,-30,29,-48,15,-50,-47,-28,-21,38],[45,48,-1,-18,9,-4,-13,10,9,8,-41],[-42,-35,20,-17,10,5,36,47,6,1,8],[3,-50,-23,16,31,2,-39,36,-25,-30,37],[-48,-41,18,-31,-48,-1,-42,-3,-8,-29,-2],[17,0,31,-30,-43,-20,-37,-6,-43,8,19],[42,25,32,27,-2,45,12,-9,34,17,32]]
    ta = [[4,11,10,9,25,21,2,14,20,12,24],[18,5,2,1,21,25,23,22,6,24,2],[8,2,5,11,6,18,7,4,10,1,20],[19,24,9,20,23,22,4,10,21,22,11],[23,20,6,22,2,19,1,3,7,8,26],[26,27,11,7,19,9,8,20,19,14,3],[3,6,21,8,20,17,24,25,18,13,19],[17,1,9,18,22,16,4,23,8,5,25],[2,4,16,5,2,15,3,13,9,6,14],[20,13,22,6,3,7,5,12,3,14,21],[25,16,23,21,12,26,13,11,24,15,23]]
    print(Solution().matrixRankTransform(matrix))

