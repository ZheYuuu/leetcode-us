from typing import List
import functools


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        def cmp(x, y):
            if len(x) == len(y):
                return x > y
            return len(x) > len(y)

        dp = ["0" for _ in range(target + 1)]
        cost_dict = {c: str(i + 1) for i, c in enumerate(cost)}
        for i in range(target + 1):
            if i in cost_dict:
                dp[i] = cost_dict[i]
            for j in cost_dict:
                if i > j and dp[i - j] != "0":
                    tmp = dp[i - j] + cost_dict[j]
                    # tmp = "".join(sorted(tmp, reverse=True))
                    print(tmp)
                    if cmp(tmp, dp[i]):
                        dp[i] = tmp
        return dp[-1]


if __name__ == "__main__":
    # ans = Solution().largestNumber([2,4,2,5,3,2,5,5,4], 739)
    ans = Solution().largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9)
    print(ans)
