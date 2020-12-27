"""
    @Difficulty : E
    @Status     : AC
    @Time       : 2020/12/6 10:26
    @Author     : Chen Runwen
"""


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


if __name__ == '__main__':
    print(Solution().interpret())

