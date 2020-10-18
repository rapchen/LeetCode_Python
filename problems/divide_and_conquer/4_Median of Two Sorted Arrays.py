class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            n1 = nums2 # n1是短的，n2是长的
            n2 = nums1
        else:
            n1 = nums1
            n2 = nums2
        len1 = len(n1)
        len2 = len(n2)
        odd = (len1 + len2) % 2 == 1
        med = (len1 + len2 + 1)//2

        # n1 为空
        if len1 == 0:
            return n2[med - 1] if odd else (n2[med - 1] + n2[med]) / 2

        # 在一个里（n2里）
        if n1[0] >= n2[med - 1]:
            if odd:
                return n2[med - 1]
            else:
                second = n1[0] if med == len2 else n2[med]
                return (n2[med - 1] + min(second, n1[0])) / 2
        if n1[len1 - 1] <= n2[len2 - med]:
            if odd:
                return n2[len2 - med]
            else:
                first = n1[len1 - 1] if med == len2 else n2[len2 - med - 1]
                return (n2[len2 - med] + max(first, n1[len1 -1])) / 2

        # 不在一个里
        if odd:
            return self.find_odd(n1, n2, 0, len1 - 1, med - 2)
        else:
            return self.find_even(n1, n2, 0, len1 - 1, med - 1)

    def find_odd(self, n1, n2, l1, r1, total):
        """
        :param total: p1 与 p2 之和，固定
        """
        p1 = (l1 + r1) // 2
        p2 = total - p1
        if n1[p1] <= n2[p2]:
            if n2[p2] <= n1[p1 + 1]:
                return n2[p2]
            else:
                return self.find_odd(n1, n2, p1 + 1, r1, total)
        else:
            if n1[p1] <= n2[p2 + 1]:
                return n1[p1]
            else:
                return self.find_odd(n1, n2, l1, p1 - 1, total)


    def find_even(self, n1, n2, l1, r1, total):
        p1 = (l1 + r1) // 2
        p2 = total - p1
        if n1[p1] <= n2[p2]:
            if n2[p2] <= n1[p1 + 1]:
                return (n2[p2] + max(n1[p1], n2[p2 - 1])) / 2
            else:
                return self.find_even(n1, n2, p1 + 1, r1, total)
        else:
            if n1[p1] <= n2[p2 + 1]:
                return (n1[p1] + max(n2[p2], n1[p1 - 1])) / 2
            else:
                return self.find_even(n1, n2, l1, p1 - 1, total)



if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
