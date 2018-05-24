class Solution():

    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
           
        e = 0
        res = 0
        for s in range(len(start)):
            if start[s]<end[e]:
                res+=1
            else:
                e+=1
        return res


    def minMeetingRooms(self, intervals):
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms




    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x:x.start)
        heap = []
        for i in intervals:
            if heap and i.start >= heap[0]:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)