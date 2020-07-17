from collections import defaultdict

INF = float("inf")


class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E

    def printAns(self, s, dp, parent):
        print("dp")
        for row in dp:
            print(f"\t{row}")
        print("parent")
        for p in parent:
            print(f"\t{p}")
        n = len(self.V)

        # Use parent
        print(f"\nsource\t end\t distance\t path")
        for v in range(n):
            path = []
            i, k = v, n - 1
            while i != -1:
                path.append(i)
                i = parent[i][k]
                k = k - 1
            print(f"{s}\t {v}\t {dp[v][n-1]}\t {path[::-1]}")

    def printAns2(self, s, dp, parent):
        print(f"dp\n\t{dp}")
        print(f"parent\n\t{parent}")
        n = len(self.V)
        print(f"\nsource\t end\t distance\t path")
        for v in range(n):
            path = []
            i, k = v, n - 1
            while i != -1:
                path.append(i)
                i = parent[i]
            print(f"{s}\t {v}\t {dp[v]}\t {path[::-1]}")



# Single source shortest path on graph having negative edge.
def bellmanFord(G, s):
    n = len(G.V)
    neighbors = defaultdict(list)
    for k, v in G.E.items():
        for e, w in v:
            neighbors[e].append((k, w))
    parent = [[-1] * n for _ in range(n)]
    # Base Case
    dp = [[INF for _ in range(n + 1)] for _ in range(n)]
    for i in range(n):
        dp[s][i] = 0

    for k in range(1, n):
        # for v in G.V:
        #     for e, w in neighbors[v]:
        # 这个比较条件必须得加上，因为可能出现前一个邻接点正常松弛了，得到了更优的dp[v][k]
        # 此时考虑以下任一种情况：
        #   1. 下一个邻接点 e 并不能通过k-1条边到达，仍然是inf状态，说明这个点就不该拿来做松弛
        #   2. 下一个邻接点的 dp[e][k-1]+w 是小于 经过松弛后的 dp[v][k]的
        # 这时候你用傻愣愣地用这样的一个邻接点去跑 dp[v][k] = min(dp[e][k-1]+w, dp[v][k-1])，
        # 那你用上一个邻接点优化完的dp[v][k]反而被覆盖掉了...
        # 所以需要加上这样的判断条件来防止出错。
        # if dp[v][k] > w + dp[e][k - 1]:
        #     dp[v][k] = min(dp[e][k - 1] + w, dp[v][k - 1])
        # 但由于还可能会涉及到路径输出时，所以最好还是这样写
        for v in G.V:
            dp[v][k] = dp[v][k - 1]
            parent[v][k] = parent[v][k - 1]
            for e, w in neighbors[v]:
                if dp[v][k] > w + dp[e][k - 1]:
                    dp[v][k] = dp[e][k - 1] + w
                    parent[v][k] = e
    # 如何判断是否有负环？
    k = k + 1
    for v in G.V:
        dp[v][k] = dp[v][k - 1]
        for e, w in neighbors[v]:
            assert dp[v][k] <= w + dp[e][k - 1], "Exist negative circle"

    G.printAns(s, dp, parent)


# Follow up
# 可以观察到dp[v][k]只和dp[...][k-1]有关，所以可以简化为一维状态数据
def bellmanFordImproved(G, s):
    n = len(G.V)
    neighbors = defaultdict(list)
    for k, v in G.E.items():
        for e, w in v:
            neighbors[e].append((k, w))
    parent = [-1] * n
    # Base Case
    dp = [INF] * n
    dp[s] = 0

    for k in range(1, n):
        for v in G.V:
            for e, w in neighbors[v]:
                if dp[v] > dp[e] + w:
                    dp[v] = dp[e] + w
                    parent[v] = e
    for v in G.V:
        for e, w in neighbors[v]:
            assert dp[v] <= dp[e] + w, "Exist negative circle"
    G.printAns2(s, dp, parent)


if __name__ == "__main__":
    # Graph1 with negative edge
    V = [0, 1, 2, 3]
    E = {0: [(1, 5), (3, 3)], 1: [(2, 5)], 2: [(3, -9)], 3: []}
    g1 = Graph(V, E)
    # ans = bellmanFord(g1, 0)

    # Graph2 with negative edge
    V = [0, 1, 2, 3, 4]
    E = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2), (4, 2)],
        2: [],
        3: [(1, 1)],
        4: [(3, -3)],
    }
    g2 = Graph(V, E)
    # ans = bellmanFord(g2, 0)
    ans = bellmanFordImproved(g2, 0)

    # Graph3 with negative circle
    V = [0, 1, 2, 3, 4]
    E = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2), (4, -2)],
        2: [],
        3: [(1, 1)],
        4: [(3, -3)],
    }
    g3 = Graph(V, E)
    # ans = bellmanFord(g3, 0)
    ans = bellmanFordImproved(g3, 0)
