import heapq
from typing import List

# class Solution(object):
#     def maxEvents(self, events):
#         """
#         :type events: List[List[int]]
#         :rtype: int
#         """
#         events.sort(key=lambda x: (x[0], x[1]))
#         heap = []
#         i, res = 0, 0
#         for day in range(100005):
#             while heap and heap[0] < day:
#                 heapq.heappop(heap)
#             while i < len(events) and events[i][0] == day:
#                 heapq.heappush(heap, events[i][1])
#                 i += 1
#             if heap:
#                 heapq.heappop(heap)
#                 res += 1
#         return res
    
#     def maxEvents(self, events):
#         events.sort()
#         pq = []
#         i, d, res = 0,0,0
#         while(pq or i<len(events)):
#             if not pq:
#                 d = events[i][0]
#             while(i<len(events) and events[i][0]==d):
#                 heapq.heappush(pq,events[i][1])
#                 i+=1
#             heapq.heappop(pq)
#             d += 1
#             res += 1
#             while(pq and pq[0]<d):
#                 heapq.heappop(pq)
#         return res


# if __name__ == "__main__":
#     sol = Solution()
#     inputs = [
#         [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7]],
#         [[1, 10000]],
#         [[1, 2], [2, 3], [3, 4], [1, 2]],
#         [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]],
#     ]
#     for data in inputs:
#         print(sol.maxEvents(data))

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # nodes = {i:0 for i in range(n)}
        edges = {i:[] for i in range(n)} 
        for i in range(n):
            a = leftChild.pop(0)
            b = rightChild.pop(0)
            if a!=-1:
                edges[i].append(a)
                # nodes[a] += 1
            if b!=-1:
                edges[i].append((i,b))
                # nodes[b] += 1
        vis = [0 for i in range(n)]
        vis[0] = 1
        self.flag = True 
        def dfs(node):
            if not self.flag:
                return False
            for e in edges[node]:
                if vis[e]:
                    self.flag = False
                    return False
                vis[e]=1
                dfs(e)
        dfs(0)
        for v in vis:
            if v==0:
                return False
        return self.flag

    def atMostSum(self, arr, n, k): 
        _sum = 0
        cnt = 0
        maxcnt = 0
        
        for i in range(n): 
    
            # If adding current element doesn't 
            # Cross limit add it to current window 
            if ((_sum + arr[i]) <= k): 
                _sum += arr[i] 
                cnt += 1
            
            # Else, remove first element of current 
            # window and add the current element 
            elif(sum != 0): 
                _sum = _sum - arr[i - cnt] + arr[i] 
            
            # keep track of max length. 
            maxcnt = max(cnt, maxcnt) 
    
        return maxcnt 

if __name__ == "__main__":
    # Driver function 
    arr = [3,2,-1,-2,3,4] 
    n = len(arr) 
    k = 1 
    print(Solution().atMostSum(arr, n, k)) 
            
            
            

