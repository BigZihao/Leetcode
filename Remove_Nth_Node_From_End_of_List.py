Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        assert n>0
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for i in range(n):
            fast = fast.next
            assert fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


    def removeNthFromEnd2(self, head, n):
        slow = fast = self
        self.next = head
        while fast.next:
            if n:
                n-=1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return self.next

