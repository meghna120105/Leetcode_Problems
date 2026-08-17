class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def solve(l, r):
            if l >= r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            ans = 0
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left_sum += stoneValue[k]
                right_sum -= stoneValue[k]

                if left_sum < right_sum:
                    if ans >= 2 * left_sum:
                        continue

                    ans = max(
                        ans,
                        left_sum + solve(l, k)
                    )

                elif left_sum > right_sum:
                    if ans >= 2 * right_sum:
                        break

                    ans = max(
                        ans,
                        right_sum + solve(k + 1, r)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + solve(l, k),
                        right_sum + solve(k + 1, r)
                    )

            dp[l][r] = ans
            return ans

        return solve(0, n - 1)