class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(root, left):
            if not root: return 
            if left and not root.left and not root.right:
                cache[0]+=root.val
            dfs(root.left, True)
            dfs(root.right, False)

        cache = [0]
        dfs(root, False)
        return cache[0]

##  Just traverse the whole tree using stack. If the left child is leave, add it to the result.
    def sumOfLeftLeaves2(self, root):
        if not root: return 0

        s = [root]
        res = 0
        while s:
            tmp = s.pop()
            if tmp.left:
                s.append(tmp.left)
                if not tmp.left.left and not tmp.left.right:
                    res+=tmp.left.val
            if tmp.right:
                s.append(tmp.right)
        return res

    def sumOfLeftLeaves3(self, root):
        sum = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            sum+=root.left.val
        sum+= self.sumOfLeftLeaves3(root.left) + self.sumOfLeftLeaves3(root.right)
        return sum


if __name__ == "__main__":
    print(Solution().sumOfLeftLeaves())