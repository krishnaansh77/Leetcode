class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        prefix=[0]*(n+1)
        prefix[0]=0
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        i=0    
        while i<n:
            if prefix[i]==prefix[n]-prefix[i+1]:
                return i
            else:
                i+=1
        return -1