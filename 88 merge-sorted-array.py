class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p1 + p2 + 1] = nums1[p1]
                p1 -= 1
            else:
                nums1[p1 + p2 + 1] = nums2[p2]
                p2 -= 1
        if p1 == -1:
            for i in range(p2 + 1):
                nums1[i] = nums2[i]


if __name__ == '__main__':
    x = [1,3,5,6,0,0]
    x2 = [-1,4]
    n = 5
    s = "Hello World"
    print(Solution().merge(x, 4, x2, 2))
    print(x)
