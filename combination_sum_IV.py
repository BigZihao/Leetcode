class Solution(object):

    # DFS solution can only handle small cases(i.e.target<=25 && len(nums)<=5), due to large list memory usage of res.
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
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




## lets compare the coin change and the combination sum IV, they are the same 
## general summary: how many number of combinations 

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        coins.sort()  ## sort the coin break to prune brunch
        for i in range(1, amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i], dp[i-c]+1)
                else:
                    break
        return dp[-1] if dp[-1]!=MAX else -1