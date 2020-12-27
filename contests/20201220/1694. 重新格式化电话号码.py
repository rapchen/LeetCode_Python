"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/12/20 9:39
    @Author     : Chen Runwen
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        res = []
        i = -3
        for i in range(0, len(number) - 4, 3):
            res.append(number[i: i+3])
        if i + 7 == len(number):
            res += [number[i+3: i+5], number[i+5: i+7]]
        else:
            res.append(number[i+3:])
        return '-'.join(res)


if __name__ == '__main__':
    print(Solution())

