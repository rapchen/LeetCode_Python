# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        prev = head
        p = head.next
        s = {head.val}
        while p is not None:
            if p.val in s:
                prev.next = p.next
            else:
                s.add(p.val)
                prev = p
            p = p.next
        return head



if __name__ == '__main__':
    x = [1,3,5,6]
    n = 5
    s = "Hello World"
    print(Solution().climbStairs(4))
