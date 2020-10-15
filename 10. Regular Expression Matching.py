class Solution:

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s = s
        self.p = p
        self.ls = len(s)
        self.lp = len(p)
        self.m = {}
        return self.matchSuffix(0, 0)

    def matchSuffix(self, ps, pp):
        match_pp = self.m.get(pp, None)
        if match_pp is None:
            self.m[pp] = {}
            match_pp = self.m[pp]
        else:
            res = match_pp.get(ps, None)
            if res is not None:
                return res

        if pp >= self.lp:
            return ps >= self.ls
        if self.p[pp] == '.':
            if pp + 1 < self.lp and self.p[pp + 1] == '*':
                # .*
                if self.matchSuffix(ps, pp + 2):
                    match_pp[ps] = True
                    return True
                while ps < self.ls:
                    if self.matchSuffix(ps + 1, pp + 2):
                        match_pp[ps] = True
                        return True
                    ps += 1
            else:
                # .
                if ps < self.ls:
                    res = self.matchSuffix(ps + 1, pp + 1)
                    match_pp[ps] = res
                    return res
                match_pp[ps] = False
        else:
            if pp + 1 < self.lp and self.p[pp + 1] == '*':
                # a*
                if self.matchSuffix(ps, pp + 2):
                    match_pp[ps] = True
                    return True
                while ps < self.ls and self.s[ps] == self.p[pp]:
                    if self.matchSuffix(ps + 1, pp + 2):
                        match_pp[ps] = True
                        return True
                    ps += 1
            else:
                # a
                if ps < self.ls and self.s[ps] == self.p[pp]:
                    res = self.matchSuffix(ps + 1, pp + 1)
                    match_pp[ps] = res
                    return res
        match_pp[ps] = False
        return False


if __name__ == '__main__':
    x = [1, 3, 5, 6, 0, 0]
    x2 = [-1, 4]
    n = 5
    s1 = "mississippi"
    s2 = "mis*is*p*."
    print(Solution().isMatch(s1, s2))
    # print(x)
