class solution():
    def connect(self, root):
        tail = dummy = TreeLinkNode(0)
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next = root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next


# level by level traversal with a dummy head prekid. 

# root is in the current level, and kid is in the next level. prekid.next is the head in the kid level

# kid = kid.next or kid : Update kid ONLY when we actually find its next node

# runtime is around 96ms with a best runtime 88ms.

    def connect(self, root):
        prekid = kid = TreeLinkNode(0)
        while root:
            while root:
                kid.next = root.left
                kid = kid.next or kid
                kid.next = root.right
                kid = kid.next or kid
                root = root.next
            root, kid = prekid.next, prekid