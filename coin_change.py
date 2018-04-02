# Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).

# The time complexity is O(amount * coins.length) and the space complexity is O(amount)

class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX]*amount
        for i in range(1, amount+1): # amount
            dp[i] = min([dp[i-c] if i-c>=0 else MAX for c in coins])+1 #coin_length
        return [dp[amount], -1][dp[amount] == MAX]

    def coinChange(self, coins, amount):
        if amount==0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False]*(amount+1)
        visited[0] = True
        while value1:
            nc+=1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1


# First sort the coins, we will deal with big coin first

# When there is no hope to reduce total count, stop the dfs

# DFS + greedy + pruning

    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        lenc, self.res = len(coins), 2**31-1
        
        def dfs(pt, rem, count):
            if not rem:
                self.res = min(self.res, count)
            for i in range(pt, lenc):
                if coins[i] <= rem < coins[i] * (self.res-count): # if hope still exists
                    dfs(i, rem-coins[i], count+1)

        for i in range(lenc):
            dfs(i, amount, 0)
        return self.res if self.res < 2**31-1 else -1