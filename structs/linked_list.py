"""
    @Time    : 
    @Author  : Chen Runwen
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_values(values) -> "ListNode":
        if not values:
            return None
        head = ListNode(values[0])
        p = head
        for v in values[1:]:
            p.next = ListNode(v)
            p = p.next
        return head

    def get_values(self) -> list:
        res = [self.val]
        p = self.next
        while p:
            res.append(p.val)
            p = p.next
        return res

    def __str__(self):
        return str(self.get_values())
