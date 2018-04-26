## time complexity O(2^n)

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([], nums, 0, res)
        return res

    def dfs(self, path, nums, index, res):
        path.sort()
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):    ##any subset, combination use index
            self.dfs(path+[nums[i]], nums, i+1, res)  ## i+1 means don't use the same item twice



    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs([], nums, res)
        return res

    def dfs(self, path, nums, res):
        path.sort()
        if path not in res:
            res.append(path)
        for i in range( len(nums)):    ##any subset, combination use index
            self.dfs(path+[nums[i]], nums[i+1:], res)  ## i+1 means don't use the same item twice