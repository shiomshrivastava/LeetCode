class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i]: best score diff (mover - opponent) using stoneValue[i:]

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            total = 0
            for k in range(1, 4):          # try taking 1, 2, or 3 stones
                if i + k > n:
                    break
                total += stoneValue[i + k - 1]
                best = max(best, total - dp[i + k])
            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"