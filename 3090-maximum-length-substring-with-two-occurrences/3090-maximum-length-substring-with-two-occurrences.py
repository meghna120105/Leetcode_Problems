class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        f = [0] * 26

        l = 0
        for r in range(n):
            f[ord(s[r]) - ord('a')] += 1

            while f[ord(s[r]) - ord('a')] > 2:
                f[ord(s[l]) - ord('a')] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res