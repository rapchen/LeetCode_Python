"""
    @Difficulty : M 1
    @Status     : AC
    @Time       : 2021/1/10 10:29
    @Author     : Chen Runwen
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        n = 0
        while p:
            p = p.next
            n += 1

        p = head
        for i in range(k - 1):
            p = p.next
        q = head
        for i in range(n - k):
            q = q.next

        p.val, q.val = q.val, p.val
        return head


if __name__ == '__main__':
    print(Solution())
