class Solution(object):
    def longestConsecutive(self, nums):
        nums=set(nums)
        largest=0
        for x in nums:
            count=1
            
            if x-1 not in nums:
                while x+count in nums:
                    count+=1
                largest=max(largest,count)
        return largest