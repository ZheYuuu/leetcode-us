'''
https://leetcode.com/problems/stone-game-iii/

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.
'''
from typing import List
class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        inf = 10e7
        pre = [sum(stoneValue)]
        n = len(stoneValue)
        if n==1:
            if stoneValue[0]>0:
                return 'Alice'
            elif stoneValue[0]==0:
                return 'Tie'
            else:
                return 'Bob'
        if n==2:
            if sum(stoneValue)>0:
                return 'Alice'
            if stoneValue[0]>stoneValue[1]:
                return 'Alice'
            elif stoneValue[0]<stoneValue[1]:
                if sum(stoneValue)==0:
                    return 'Tie'
                return 'Bob'
            else:
                return 'Tie'


                
        for v in stoneValue[:-1]:
            pre.append(pre[-1]-v)
        # base case
        dp = [-inf for _ in range(n)]
        dp[n-1] = pre[n-1]
        dp[n-2] = max(pre[n-2]-dp[n-1], pre[n-2])
        dp[n-3] = max(pre[n-3]-dp[n-2], pre[n-3]-dp[n-1], pre[n-3])
        # recurrence relation
        for i in reversed(range(n-3)):
            dp[i] = max(pre[i]-dp[i+1], pre[i]-dp[i+2],pre[i]-dp[i+3])
        if 2*dp[0]>pre[0]:
            return 'Alice'
        elif 2*dp[0]<pre[0]:
            return 'Bob'
        else:
            return 'Tie'

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        inf = 10e7
        sumv = 0
        n = len(stoneValue)
        dp = [-inf for _ in range(n+1)]
        dp[-1] = 0
        for i in reversed(range(n)):
            sumv = sumv+stoneValue[i]
            for k in range(1,4):
                if i+k>n:
                    break
                dp[i] = max(sumv-dp[i+k], dp[i])
        if 2*dp[0]>sumv:
            return 'Alice'
        elif 2*dp[0]<sumv:
            return 'Bob'
        else:
            return 'Tie'


if __name__ == "__main__":
    t = Solution().stoneGameIII([-2,1,3])
    print(t)