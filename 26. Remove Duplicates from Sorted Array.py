class Solution(object):
    def remove_duplicates(self, nums):
        if not nums:
            return 0
        unique_index = 0

        for i in range(1, len(nums)):
            # Check if the current number is different from the last unique number
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]

        # The number of unique elements is unique_index + 1
        return unique_index + 1

