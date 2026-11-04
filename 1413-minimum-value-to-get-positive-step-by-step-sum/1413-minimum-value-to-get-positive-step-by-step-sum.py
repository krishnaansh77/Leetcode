class Solution(object):
    def minStartValue(self, nums):
        prefix=[0]*(len(nums)+1)
        minfix=prefix[0]
        
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
            if prefix[i+1]<minfix:
                minfix=prefix[i+1]
        if minfix<0:
            return 1-minfix
        else:
            return 1

        
        