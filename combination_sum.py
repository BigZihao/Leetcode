class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(candidates, target, index, path, res):
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(candidates)):
            if candidates[i]>target:
                break
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)


    def combinationSum2(self, candidates, target):
        candidates.sort()
        stack = [(0,0,[])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for n in range(start, len(candidates)):
                t = total + candidates[n]
                if t > target:
                    break
                stack.append((t, n, res + [candidates[n]]))
        return result

    def combinationSum3(self, candidates, target):
        candidates.sort()
        dp = [[[]]] + ([] for _ in range(target))
        for i in range(1, target + 1):
            for number in candidates:
                if number > i: break
                for L in dp[i-number]:
                    if not L or number >= L[-1]: dp[i]+=L+[number],
        return dp[-1]