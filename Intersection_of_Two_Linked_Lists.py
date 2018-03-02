class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

            ## the most important thing is switch the head node
            ## it’s O(a+b)

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# the idea is if you switch head, the possible difference between length would be countered. 
# On the second traversal, they either hit or miss. 
# if they meet, pa or pb would be the node we are looking for, 
# if they didn't meet, they will hit the end at the same iteration, pa == pb == None, return either one of them is the same,None
# @utsavvakil the time complexity is still O(N) even if he traverses the list twice. O(2N) is just O(N) because we can drop the coefficient. 
# Space complexity is constance O(1) because he is only keeping track of 2 nodes. Hope this helps.


this is very simliar to the linked list cycle, this is two differnt pointer on the same Linked List 

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow!= fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
