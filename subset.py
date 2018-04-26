class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([], nums, 0, res)
        return res

    def dfs(self, path, nums,index, res):
        res.append(path)
        for i in range(index, len(nums)):    ##any subset, combination use index
            self.dfs(path+[nums[i]], nums, i+1, res)  ## i+1 means don't use the same item twice