def memorize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

        
class Solution(object):

## recursion 

    def uniquePaths1(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths1(m-1,n) + self.uniquePaths1(m, n-1) 

    @memorize
    def uniquePaths3(self, m, n):
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths1(m-1,n) + self.uniquePaths1(m, n-1) 

## bottom-up
    def uniquePaths2(self, m, n):
        res = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]

    def uniquePaths4(self, m, n):
        if m<n:
            m, n = n, m
        mul = lambda x, y: reduce(operator.mul, range(x, y), 1)
        return mul(m, m+n-1)/mul(1, n)


#很常见的小学生奥数题，可以用排列组合来求解，一共要走(m-1)+(n-1)步，其中(m-1)步向下，(n-1)向右，且有公式 mCn = n!/m!(n-m)! ，那么可以用下面的代码求解：
    def uniquePaths5(self, m, n):
        m-=1
        n-=1
        return math.factorial(m+n) / (math.factorial(n) * math.factorial(m))



import time
from functools import reduce
import operator
import math

if __name__ == '__main__':
    start_time = time.time()
    print(Solution().uniquePaths1(15, 12))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(Solution().uniquePaths2(15, 12))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(Solution().uniquePaths3(15, 12))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(Solution().uniquePaths4(15, 12))
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    print(Solution().uniquePaths5(15, 12))
    print("--- %s seconds ---" % (time.time() - start_time))