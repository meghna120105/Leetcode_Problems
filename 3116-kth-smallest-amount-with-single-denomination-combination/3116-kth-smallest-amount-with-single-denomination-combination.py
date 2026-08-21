from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            ans = 0
            for mask in range(1, 1 << n):
                multiple = 1
                cnt = 0
                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        cnt += 1
                        if multiple > x:
                            break
                if multiple > x:
                    continue
                ans += x // multiple if cnt % 2 else -(x // multiple)
            return ans

        low, high = 1, min(coins) * k

        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low