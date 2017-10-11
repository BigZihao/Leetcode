
class Solution(object):
## recursion
## takes O(2^n) time, TLE
    def climbstairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbstairs(n - 1) + self.climbstairs(n - 2)



## bottom up, O(n) space
    def climbstairs2(self, n):
        if n == 1:
            return 1
        res = [0 for i in range(n)]
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-2] + res[i-1]
        return res[-1]


## look at the topological order, only need O(1) space
    def climbstairs3(self, n):
        if n == 1:
            return 1
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b 



import time

if __name__ == "__main__":
    start_time = time.time()
    assert Solution().climbstairs(35) 
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    assert Solution().climbstairs2(35) 
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    assert Solution().climbstairs3(35) 
    print("--- %s seconds ---" % (time.time() - start_time))

