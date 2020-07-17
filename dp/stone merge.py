# 随机石子合并
# 贪心，每次选最小的两堆合并。原理类似huffman tree

# 线性石子合并
inf = float("inf")


def mergeStoneArray(stones):
    n = len(stones)
    dp = [[inf] * n for _ in range(n)]
    prefix = [0]
    for stone in stones:
        prefix.append(prefix[-1] + stone)
    for i in range(n):
        dp[i][i] = 0
    for length in range(2, n + 1):
        for i in range(n):
            j = i + length - 1
            if j >= n:
                break
            for k in range(i, j):
                dp[i][j] = min(
                    dp[i][j], dp[i][k] + dp[k + 1][j] + prefix[j + 1] - prefix[i]
                )

    return dp[0][n - 1]


# 环形石子合并
def mergeStoneRing(stones):
    n = len(stones)
    dp = [[inf] * n for _ in range(n)]
    dp2 = [[-inf] * n for _ in range(n)]
    prefix = [0]
    stones = stones + stones
    for stone in stones:
        prefix.append(prefix[-1] + stone)
    for i in range(n):
        dp[i][i] = 0
        dp2[i][i] = 0
    for length in range(2, n + 1):
        for i in range(n):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j % n] = min(
                    dp[i][j % n],
                    dp[i][k % n] + dp[(k + 1) % n][j % n] + prefix[j + 1] - prefix[i],
                )
                dp2[i][j % n] = max(
                    dp2[i][j % n],
                    dp2[i][k % n] + dp2[(k + 1) % n][j % n] + prefix[j + 1] - prefix[i],
                )

    _min = min(dp[i][(i + n - 1) % n] for i in range(n))
    _max = max(dp2[i][(i + n - 1) % n] for i in range(n))
    
    return _min, _max 


if __name__ == "__main__":
    stones = [3, 4, 6, 5, 4, 2]
    stones = [1, 3, 5, 2]
    stones = [4, 5, 9, 4]
    # ans = mergeStoneArray(stones)
    ans = mergeStoneRing(stones)
    print(ans)
