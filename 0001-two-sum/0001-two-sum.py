class Solution:
    def twoSum(self, nums, target):
        counter = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                counter += 1

                if nums[i] + nums[j] == target:
                    return [i, j]