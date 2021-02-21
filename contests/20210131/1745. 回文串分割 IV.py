"""
    @Difficulty : H
    @Status     : AC
    @Time       : 2021/1/31 10:13
    @Author     : Chen Runwen
"""
from collections import defaultdict


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        palin = defaultdict(set)
        n = len(s)

        for i in range(n):
            # 奇数
            palin[i].add(i)
            for j in range(1, n):
                if i + j >= n or i - j < 0 or s[i-j] != s[i+j]:
                    break
                palin[i-j].add(i+j)
            # 偶数
            for j in range(n):
                if i + j + 1 >= n or i - j < 0 or s[i-j] != s[i+j+1]:
                    break
                palin[i-j].add(i+j+1)

        for p in palin[0]:
            for q in palin[p + 1]:
                if n - 1 in palin[q + 1]:
                    return True

        return False


class Solution3:
    def checkPartitioning(self, s: str) -> bool:
        # 每个节点记录倒序到这的下标，还有下面的所有节点
        root = {}
        n = len(s)
        for i in range(n):
            node = root
            for j in range(i, -1, -1):
                c = s[j]
                if c not in node:
                    node[c] = ({j}, {})
                else:
                    node[c][0].add(j)
                node = node[c][1]

        palin = defaultdict(set)
        i = 0
        node = root
        last = ''
        for j in range(i, n):
            c = s[j]
            if c not in node:
                break
            if j in node[c][0]:
                palin[i].add(j * 2 - i)
            if j - 1 in node[c][0] and c == last:
                palin[i].add(j * 2 - i - 1)
            node = node[c][1]
            last = c

        for i1 in palin[0]:
            i = i1 + 1
            node = root
            last = ''
            for j in range(i, n):
                c = s[j]
                if c not in node:
                    break
                if j in node[c][0]:
                    palin[i].add(j * 2 - i)
                if j - 1 in node[c][0] and c == last:
                    palin[i].add(j * 2 - i - 1)
                node = node[c][1]
                last = c

        n = len(s)
        for p in palin[0]:
            for q in palin[p + 1]:
                if n - 1 in palin[q + 1]:
                    return True

        return False


class Solution1:
    def checkPartitioning(self, s: str) -> bool:
        s1 = '{'.join(s)
        # 每个节点记录倒序到这的下标，还有下面的所有节点
        root = [None] * 27
        n = len(s1)
        for i in range(n):
            if s1[i] == '{':
                continue
            node = root
            for j in range(i, -1, -1):
                c = ord(s1[j]) - 97
                if not node[c]:
                    node[c] = ({j}, [None] * 27)
                else:
                    node[c][0].add(j)
                node = node[c][1]

        palin = defaultdict(set)
        for i in range(n):
            node = root
            for j in range(i, n):
                c = ord(s1[j]) - 97
                if not node[c]:
                    break
                if j in node[c][0]:
                    palin[i // 2].add(j - i // 2)
                node = node[c][1]

        n = len(s)
        for p in palin[0]:
            for q in palin[p + 1]:
                if n - 1 in palin[q + 1]:
                    return True

        return False


class Solution2:
    def checkPartitioning(self, s: str) -> bool:
        s1 = '#'.join(s)

        # 每个节点记录倒序到这的下标，还有下面的所有节点
        root = {}
        n = len(s1)
        for i in range(n):
            if s1[i] == '#':
                continue
            node = root
            for j in range(i, -1, -1):
                c = s1[j]
                if c not in node:
                    node[c] = ({j}, {})
                else:
                    node[c][0].add(j)
                node = node[c][1]

        palin = defaultdict(set)
        for i in range(n):
            node = root
            for j in range(i, n):
                c = s1[j]
                if c not in node:
                    break
                if j in node[c][0]:
                    palin[i // 2].add(j - i // 2)
                node = node[c][1]

        n = len(s)
        for p in palin[0]:
            for q in palin[p + 1]:
                if n - 1 in palin[q + 1]:
                    return True

        return False


if __name__ == '__main__':
    # s="lozeukvpvhjgrpkyyntkxppbhrscfplnnycmwjtrkdwgercawyggpiakhbnkcnezkhkveiqgymbhjolellyuxtupbyyxtqotdcrzkuvsmszjmpsrlalnawjnekpsgvobnucjwfcdsrmbjghsevaqegejwwigpiyjhyqszbtrjngqbtvwadmlpyqtisgbwjqpvzeaqidbxbafyhnirsjwjmmabsorfsxjwaebjwfebxxiqresccserqixxbefwjbeawjxsfrosbammjwjsrinhyfabxbdiqaezvpqjwbgsitqyplmdawvtbqgnjrtbzsqyhjyipgiwwjegeqaveshgjbmrsdcfwjcunbovgspkenjwanlalrspmjzsmsvukzrcdtoqtxyybputxuyllelojhbmygqievkhkzencknbhkaipggywacregwdkrtjwmcynnlpfcsrhbppxktnyykprgjhvpvkuezolbnvbmqhdyrhczdeeksgfhrdntwdgosopitiukxakwqnacgsappasgcanqwkaxkuitiposogdwtndrhfgskeedzchrydhqmbvnbvpyztexbxetzypv"
    s = "bcbddxy"
    print(Solution().checkPartitioning(s))
