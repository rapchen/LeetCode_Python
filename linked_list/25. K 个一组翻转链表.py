"""
    @Time    : 
    @Author  : Chen Runwen
"""
from structs.linked_list import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 1:
            return head

        # p0: 这k个之前的那个结点。p1: 当前结点前一个，p2: 当前结点，p3: 当前结点后一个。phead: head的前一个节点，用于返回
        p0 = phead = ListNode(0)
        phead.next = head
        p2 = head

        while p2 is not None:
            p1 = None
            for i in range(k):
                # 看看是不是到末尾了，如果到末尾了就把这一段再反转回去
                if p2 is None:
                    while p1 is not None:
                        p3 = p1.next
                        p1.next = p2
                        p2 = p1
                        p1 = p3
                    return phead.next

                # 还没到末尾，正常反转这一个结点
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3

            # k个结点反转结束了，把前一段跟这一段连起来
            p3 = p0.next
            p0.next = p1
            p0 = p3
            p0.next = p2

        return phead.next


if __name__ == '__main__':
    head = ListNode.from_values([1,2])
    k = 3
    print(Solution().reverseKGroup(head, k).get_values())
