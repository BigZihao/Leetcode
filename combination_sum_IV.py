class Solution(object):

    # DFS solution can only handle small cases(i.e.target<=25 && len(nums)<=5), due to large list memory usage of res.
    def combinationSum(self, nums, target):
        nums.sort()
        res = []
        self.dfs(nums, target, 0, [], res)
        return res


    def dfs(nums, target, indx, path, res):
        if target==0:
            res.append(path)
            return
        for i in range(len(nums)):
            if nums[i]>target:
                break
            self.dfs(nums, target - nums[i], i, path +[nums[i]], res)


## when we only care about number, it can be reduce to a simpler problem
    def combinationSum2(self, nums, target):
        nums.sort()
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    break
                dp[i]+=dp[i-num]
        return dp[target]




