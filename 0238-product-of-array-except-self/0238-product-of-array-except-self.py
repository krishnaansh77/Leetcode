class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        
        
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix=prefix*nums[i]

        
        suffix=1
        for j in range(n-1,-1,-1):
            
            ans[j]=suffix*ans[j]
            suffix=suffix*nums[j]
            


        
        return ans