class Solution:
    def sortedSquares(self, nums):

        neg = []
        pos = []

        # Separate negative and positive numbers
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        # Case 1: No negative numbers
        if len(neg) == 0:
            for i in range(len(pos)):
                pos[i] = pos[i] * pos[i]
            return pos

        # Case 2: No positive numbers
        if len(pos) == 0:
            for i in range(len(neg)):
                neg[i] = neg[i] * neg[i]

            neg.reverse()
            return neg

        # Case 3: Both negative and positive numbers exist

        # Square negative numbers
        for i in range(len(neg)):
            neg[i] = neg[i] * neg[i]

        # Square positive numbers
        for i in range(len(pos)):
            pos[i] = pos[i] * pos[i]

        # Reverse negative array
        neg.reverse()

        # Merge both arrays
        ans = []
        i = 0
        j = 0

        while i < len(neg) and j < len(pos):

            if neg[i] < pos[j]:
                ans.append(neg[i])
                i += 1
            else:
                ans.append(pos[j])
                j += 1

        # Remaining negative numbers
        while i < len(neg):
            ans.append(neg[i])
            i += 1

        # Remaining positive numbers
        while j < len(pos):
            ans.append(pos[j])
            j += 1

        return ans