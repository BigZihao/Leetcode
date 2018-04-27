search
backtracking
Subsets, Combination and Permutation

1. Permutation

start with any element and dfs to all the rest. will have [1,2] [2,1] both in res

2. subset and combinatio are same problem, there is no order sepecific path in res. so use index
Combination 类问题是典型的搜索问题，除了 DFS + backtracking 之外，combination 里最重要的就是“去重”，
怎么让自己的搜索树不回头地往前走。
we only want [1,2] in res

Combination 类问题最重要的是去重， dfs() 函数里带一个 index 参数可以很好的解决这个问题。
顺序问题中有“单序列”和“全序列”顺序，分别对应一个序列中元素的顺序和整个序列中子序列顺序。
可以通过子序列翻转或者全局翻转操作，利用两次翻转相互抵消的特点解决序列顺序问题。



3. DFS has connection with DP


1. Permutation
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



2.1 subsets
    def subsets(self, nums):
        res = []
        self.dfs([], nums, 0, res)
        return res
    def dfs(self, path, nums,index, res):
        res.append(path)
        for i in range(index, len(nums)):    ##any subset, combination use index
            self.dfs(path+[nums[i]], nums, i+1, res)  ## i+1 means don't use the same item twice

2.2 combination
这类题的搜索树都是极度向左倾斜的结构，节点数为 2^n;
it subset adding a parameter to only include those subset with length k

    def combine(self, n, k):
        res = []
        self.dfs(xrange(1,n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
    	if k == 0:
            res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)

## actually this works as well, but the above one is significantly faster
## from this point of view, combination is just a special case of subset
## but since its special case, we can prune the search path and increase the efficiency
## this is called backtracking
## its backtracking within DFS search

    def dfs(self, nums, k, index, path, res):
        if k > len(nums) - index + 1: return  ## to save some time. or prune search path
        elif k == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)



3. connection with DP
   def combinationSum4(self, nums, target):
        nums.sort()
        res = []
        self.dfs(nums, target, [], res)
        return len(res)
    
    def dfs(self, nums, target, path, res):
        if target<0:
            return
        if target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums, target - nums[i], path+[nums[i]], res)


## when we only care about number, it can be reduce to a simpler problem
## become basically the coin change probelm
## O(nlogn + target*n)
    def combinationSum2(self, nums, target):
        nums.sort()
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i:  ## dp can do prune brunch as well
                    break
                dp[i]+=dp[i-num]
        return dp[target]
