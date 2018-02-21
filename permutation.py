##Given a collection of distinct numbers, return all possible permutations.
## 这道题是求全排列问题，给的输入数组没有重复项，这跟之前的那道 Combinations 组合项 和类似，解法基本相同，
#但是不同点在于那道不同的数字顺序只算一种，是一道典型的组合题，而此题是求全排列问题，还是用递归DFS来求解。
#这里我们需要用到一个visited数组来标记某个数字是否访问过，然后在DFS递归函数从的循环应从头开始，而不是从level开始，
#这是和 Combinations 组合项 不同的地方，其余思路大体相同，代码如下：


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
    # Use reduce to insert the next number anywhere in the already built permutations.
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

    def permute6(self, nums):
        perms = [[]]
        for n in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm)+1):
                    new_perm.append(perm[:i]+[n]+perm[i:])
            perms = new_perm 
        return perms


from functools import reduce
if __name__ == "__main__":
    print(Solution().permute([1,2,3]))
    print(Solution().permute2([1,2,3]))
    print(Solution().permute3([1,2,3]))
    print(Solution().permute4([1,2,3]))
    print(Solution().permute5([1,2,3]))
    print(Solution().permute6([1,2,3]))



