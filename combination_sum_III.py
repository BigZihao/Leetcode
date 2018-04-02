class Solution(object):
    def combinationSum(self, k, n):
        res = []
        self.dfs(range(1,10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k == 0 and n == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, n - nums[i], i + 1, path+[nums[i]], res)
