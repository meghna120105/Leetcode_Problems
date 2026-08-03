class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            running_sum = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                running_sum += stoneValue[i + k - 1]
                best = max(best, running_sum - dp[i + k])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"