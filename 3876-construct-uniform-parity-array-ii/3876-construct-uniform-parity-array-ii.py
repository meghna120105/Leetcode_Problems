class Solution:
    def uniformArray(self, nums):
        smallestOdd = float('inf')

        for num in nums:
            if num % 2 == 1:
                smallestOdd = min(smallestOdd, num)

        # Already all even
        if smallestOdd == float('inf'):
            return True

        # Check whether every even number can become odd
        for num in nums:
            if num % 2 == 0 and num <= smallestOdd:
                return False

        return True