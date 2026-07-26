class Solution:
    def maximumProduct(self, A: list[int]) -> int:
        n = len(A)

        for i in range(2):
            k = i
            for j in range(i + 1, n):
                if A[j] < A[k]:
                    k = j
            A[i], A[k] = A[k], A[i]

        for i in range(n - 1, max(-1, n - 4), -1):
            k = i
            for j in range(i):
                if A[j] > A[k]:
                    k = j
            A[i], A[k] = A[k], A[i]

        return max(
            A[-1] * A[-2] * A[-3],
            A[-1] * A[0] * A[1]
        )