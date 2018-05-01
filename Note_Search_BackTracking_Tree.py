
Search
Tree and BackTracking 

普遍要求返回 “所有解” ，大多为暴力穷举，本质上是划出搜索结构树做 DFS.

1. DFS in tree is essentially pre-order traversal
2. DFS in tree is just left and right, DFS in general search path "tree" should loop over all nums,
and here nums serve as visited, cause when one element is visited will be deleted from nums in later 
search path


DFS + Backtracking 都有三个步骤：
Add element
DFS and Remove element


1.1 DFS in tree is essentially pre-order traversal

class preOrderTraversalUsingDFS():
		# recursively
	def preorderTraversal1(self, root):
	    res = []
	    self.dfs(root, res)
	    return res
	    
	def dfs(self, root, res):
	    if root:
	        res.append(root.val)
	        self.dfs(root.left, res)
	        self.dfs(root.right, res)


1.2  DFS binaryTreePaths

# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res

def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
    if root.left:
        self.dfs(root.left, ls+str(root.val)+"->", res)
    if root.right:
        self.dfs(root.right, ls+str(root.val)+"->", res)


1.3 generate parenthesis

too trivial. 这题和二叉树其实挺像的，因为在每一个位置都只有两种可能 "(" 和 ")".

def generateParethesis(self, n):
    if not n:
        return []
    left, right, res = n, n, []
    self.dfs(left, right, "", res)
def dfs(self, left, right, path, res):
    if right<left:
        return
    if not left and not right:
        res.append(path)
    if left:
        self.dfs(left-1, right, path+"(", res)
    if right:
        self.dfs(left, right-1, path+")", res)



2. DFS in general search path "tree"

class Permutation():
   # DFS
    def permute3(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            print(res)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)






            