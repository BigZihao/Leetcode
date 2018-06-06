class Solution():
    def searchMatrix(self, matrix, target):
        m, n, r, c = len(matrix), len(matrix[0]), 0, n-1
        while r<m and c >=0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][t] > target:
                c-=1
            else:
                r+=1
        return False