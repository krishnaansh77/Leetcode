class Solution(object):
    def findMiddleIndex(self, nums):
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        
        for j in range(n):
            if prefix[j]==prefix[n]-prefix[j+1]:
                return j
        return -1
        
        