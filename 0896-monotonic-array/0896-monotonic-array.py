class Solution(object):
    def isMonotonic(self, nums):
        n=len(nums)
        count=1
        increase=True
        decrease=True
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                count=count+1
            if nums[i]>nums[i+1]:
                increase=False
            if nums[i]<nums[i+1]:
                decrease=False

        if count==n:
            return True
        return increase or decrease 
