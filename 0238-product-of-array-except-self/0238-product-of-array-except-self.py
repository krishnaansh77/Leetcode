class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[]
        
        prefix=[1]*len(nums)
        prev=1
        for i in range(n):
            prefix[i]=prev
            prev=prefix[i]*nums[i]

        suffix=[1]*len(nums)
        prev=1
        for j in range(n-1,-1,-1):
            suffix[j]=prev
            prev=suffix[j]*nums[j]


        for k in range(n):
            ans.append(prefix[k]*suffix[k])

        return ans