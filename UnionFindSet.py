class UnionFindSet:
    def __init__(self, n):
        self.ranks = [1 for _ in range(n)]
        self.parents = [1 for _ in range(n)]
        self.count = n

    def find(self, k):
        if k != self.parents[k]:
            self.parents[k] = self.find(self.parents[k])
        return self.parents[k]
    
    def union(self, a, b):
        aRoot = self.find(a)
        bRoot = self.find(b)
        if aRoot==bRoot:
            return 
        if self.ranks[aRoot]>self.ranks[bRoot]:
            self.parents[bRoot] = self.parents[aRoot]
        elif self.ranks[aRoot]<self.ranks[bRoot]:
            self.parents[aRoot] = self.parents[bRoot]
        else:
            self.parents[aRoot] = bRoot
            self.ranks[bRoot] += 1

if __name__ == "__main__":
    sol = Solution()
