class Solution(object):

## O(Nloglog(N))  O(N)
    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                ##  将i的2倍、3倍、4倍...都标记为非素数
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        return sum(primes)


import numpy as np
if __name__ == "__main__":
    print(Solution().countPrimes(20))