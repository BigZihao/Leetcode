class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp, maxArea = [[0 for _1_ in range(len(matrix[0]))] for ___ in range(len(matrix))], 0
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[0])):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                maxArea = max(maxArea, dp[i][j])
        return maxArea*maxArea


    def maximalSquare2(self, A):
        for i, r in enumerate(A):
            r = A[i] = map(int, r)
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(A[i-1][j], r[j-1], A[i-1][j-1]) + 1
        return max(map(max, A + [[0]])) ** 2


#We define dp[i][j] the maximal ending at position (i, j). Thus, current state (dp[i][j])depends on left (dp[i][j - 1]), up (dp[i - 1][j]), and left-up’s (dp[i - 1][j - 1]) states. The current state equals to the minimum of these three states plus matrix[i][j] because any smaller value will lead to a smaller square (holes in somewhere). I use maxArea to track the maximal square. When matrix[i][j] == '0', the maximal square ending at position (i, j) is obviously 0.

#Recurrence relation:

#For matrix[i][j] == 1, dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + int(matrix[i][j]).

#For matrix[i][j] == 0, dp[i][j] = 0