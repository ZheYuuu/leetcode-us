from collections import defaultdict
inf = float("inf")
class Graph:
    def __init__(self, V, E):
        self.V = V 
        self.E = {v:[] for v in V} 
        self.W = {}
        for u,v,w in E:
            self.E[u].append(v)
            self.W[(u,v)] = w
    
    def printAns(self, dp, parent):
        n = len(self.V)
        print("dp")
        for row in dp[n]:
            print(f"\t{row}")
        print(f"start\tend\tdistance\tpath")
        for i in range(n):
            for j in range(n):
                print(f"{i}\t{j}\t{dp[n][i][j]}")
    
    def printAns2(self, dp, path):
        print("dp")
        n = len(self.V)
        for row in dp:
            print(f"\t{row}")
        print(f"start\tend\tdistance\tpath")
        for i in range(n):
            for j in range(n):
                _path = [i]
                k = path[i][j]
                while(k!=-1):
                    _path.append(k)
                    k = path[k][j]
                _path.append(j)
                print(f"{i}\t{j}\t{dp[i][j]}\t{_path}")

def floyd(G):
    n = len(G.V)
    dp = [[[inf]*n for _ in range(n)] for _ in range(n+1)]
    # Base Case:
    for i, edges in G.E.items():
        dp[0][i][i] = 0
        for j in edges:
            dp[0][i][j] = G.W[(i,j)]
    # Tabulation:
    for k in range(1,n+1):
        for i in range(n):
            for j in range(n):
                # if dp[k][i][j]>dp[k-1][i][k-1]+dp[k-1][k-1][j]:
                dp[k][i][j] = min(dp[k][i][j], dp[k-1][i][j], dp[k-1][i][k-1]+dp[k-1][k-1][j])
    G.printAns(dp, None)

def floydImproved(G):
    n = len(G.V)
    dp = [[inf]*n for _ in range(n)]
    path = [[-1]*n for _ in range(n)]
    for i,edges in G.E.items():
        dp[i][i] = 0
        for j in edges:
            dp[i][j] = G.W[(i,j)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][j]>dp[i][k]+dp[k][j]:
                    dp[i][j] = dp[i][k]+dp[k][j]
                    path[i][j] =k 
        for i in range(n):
            assert dp[i][i]>=0, "Exist negative circle"
                
    G.printAns2(dp, path)

if __name__ == "__main__":
    # Graph 1 with all positive edge
    V = [0,1,2,3]
    E = [[0,2,8],[0,3,1],[1,2,1],[2,0,4],[3,1,2],[3,2,9]]
    g1 = Graph(V,E)
    # floyd(g1)
    # floydImproved(g1)

    # Graph 2 with negative circle
    V = [0,1,2,3,4]
    E = [[0,1,-1],[0,2,4],[1,4,-2],[1,3,2],[1,2,3],[3,1,1],[3,2,5],[4,3,-3]]
    g2 = Graph(V,E)
    floydImproved(g2)


