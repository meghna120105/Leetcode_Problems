class Solution:
    def minSumOfLengths(self, A: List[int], target: int) -> int:
        n = len(A)
        res, tot, j = n + 1, 0, 0

        dp = [n] * (n + 1)

        for i in range(n):
            tot += A[i]

            while tot > target:
                tot -= A[j]
                j += 1
            dp[i + 1] = dp[i]

            if tot == target:
                Len = i - j + 1
                res = min(res, Len + dp[j])
                dp[i + 1] = min(dp[i], Len)

        return -1 if res == n + 1 else res