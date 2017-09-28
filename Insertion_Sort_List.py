

## time O(N^2) space O(1)
## insertion sort take O(N^2) time, even though it's slightly better than selection sort


def insertionSortList(self, head):
	cur = dummy = ListNode(0)
	while head:
		if cur and cur.val > head.val:  # reset pointer only when new number is smaller than pointer value
			cur = dummy
		while cur.next and cur.next.val < head.val: # classic insertion sort to find position
			cur = cur.next
		cur.next, cur.next.next, head = head, cur.next, head.next  # insert
	return dummy.next


## It calculate all values before assignment, so you can not do it line by line.
## if do it line by line, need a new variable 




def insertionSortList(self, head):
	dummy = ListNode(0)

	while head:
		temp = dummy
		next = head.next 
		while temp.next and temp.next.val < head.val:
			temp = temp.next
		head.next = temp.next
		temp.next = head
		head = next
	return dummy.next



## Option 3 actually didn't pass the TLE 

def insertionSortList(self, head):
    if not head:
        return head
    dummy = ListNode(0)                         #为链表加一个头节点
    dummy.next = head
    curr = head
    while curr.next:
        if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
            pre = dummy                         #直到一个节点的值小于前面节点的值
            while pre.next.val < curr.next.val: #然后寻找插入的位置
                pre = pre.next
            tmp = curr.next                     #上面的示意图就是以下这段代码
            curr.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
        else:
            curr = curr.next
    return dummy.next


