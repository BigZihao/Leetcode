class Solution(object):
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(None)
        dummy.next = head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next


    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre, cur = dummy, head
        count=0
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
                count+=1
            elif count!=0:
                pre.next = cur.next
                cur = cur.next
                count=0
            else:
                cur = cur.next
                pre = pre.next
        return dummy.next