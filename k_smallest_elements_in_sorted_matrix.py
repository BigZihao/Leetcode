##  Heap solution gives me 176 ms. 
## The time complexity is O(k * log n), 
## so the worst-case and average-case time complexity is O(n^2 * log n). 
## Space complexity is O(n).

class solution():
    def kthSmallest(self, matrix, k):
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
