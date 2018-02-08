class Solution(object):

    # recursion
    # Take any number as the first number and append any permutation of the other numbers.
    def permute(self, nums):
        return [[n] + p
            for i, n in enumerate(nums)
            for p in self.permute(nums[:i] + nums[i+1:])] or [[]]

    def permute1(self, nums):
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        res = []
        for i in range(len(nums)):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]+j])
        return res


    # reduce
    def permute2(self, nums):
        return reduce(lambda P, n: [p[:i] + [n] +p[i:] 
            for p in P for i in range(len(p)+1)], nums, [[]])

    # DFS
    def permute3(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)

    # iteration
    def permute4(self, nums):
        result = [nums]
        for i in range(len(nums)-1):
            for one in result[:]:
                for j in range(i+1, len(nums)):
                    result.append(one[:i] + one[j:] + one[i:j])
        return result

    # backtracking
    def permute5(self, nums):
        res = []
        max = len(nums)
        self.helper(res, [], nums, 0, max)
        return res

    def helper(self, res, l, r, n, max):
        if n == max:
            res.append(l)
        for i in range(0, len(r)):
            self.helper(res, l+[r[i]], r[:i]+r[i+1:], n+1, max)


from functools import reduce
if __name__ == "__main__":
    print(Solution().permute([1,2,3]))
    print(Solution().permute2([1,2,3]))
    print(Solution().permute3([1,2,3]))
    print(Solution().permute4([1,2,3]))
    print(Solution().permute5([1,2,3]))



