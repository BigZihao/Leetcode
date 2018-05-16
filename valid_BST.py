
class Solution(object):
    ### inorder traversal
    def isValidBST(self, root):
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False 
        return True

    def inorder(self, root, output):
        if root is None:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

    def isValidBST2(self, root, lessThan = float('inf'), largerThan = float('-inf')):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False 
        return self.isValidBST2(root.left, min(lessThan, root.val), largerThan) and self.isValidBST2(root.right, lessThan, max(root.val, largerThan))


if '__name__' == '__main__':