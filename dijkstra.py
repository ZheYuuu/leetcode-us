import heapq
from collections import defaultdict

class Dijkstra:
    def __init(self):
        pass

    def heapVersion(self, adjmat, weights, start, n):
        s = set()
        pq = [(0, start)]
        dis = {}
        for i in range(n):
            dis[i] = float("inf")
        dis[start] = 0
        while(pq):
            d, u = heapq.heappop(pq) 
            s.add(u)
            for v in adjmat[u]:
                # 用u来进行start到v的松弛.
                newd = d+weights[u][v]
                if v not in s and newd < dis[v]:
                    dis[v] = newd
                    heapq.heappush(pq, (newd, v))
            print(pq)
        print("dis: ", dis)
        return dis


if __name__ == "__main__":
    n = 6
    adjmat = defaultdict(list)
    weights = defaultdict(dict)
    edges = [(0,1,4),(0,5,1),(0,4,3),(1,2,1),(1,3,3),(1,4,1),(1,5,2),(2,3,1),(2,4,4),(3,4,6),(4,5,1)]
    for u,v,w in edges:
        adjmat[u].append(v)
        adjmat[v].append(u)
        weights[u][v] = w
        weights[v][u] = w
    Dijkstra().heapVersion(adjmat, weights, 0, n)
