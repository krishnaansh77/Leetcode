class Solution(object):
    def longestConsecutive(self, nums):
        num = list(set(nums))
        sorted_array = sorted(num)

        if len(sorted_array) == 0:
            return 0

        count = 1
        max_count = 1

        for i in range(len(sorted_array) - 1):

            if sorted_array[i + 1] == sorted_array[i] + 1:
                count += 1

            else:
                if count > max_count:
                    max_count = count

                count = 1

        # Check the last sequence
        if count > max_count:
            max_count = count

        return max_count