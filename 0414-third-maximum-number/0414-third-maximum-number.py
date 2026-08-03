class Solution(object):
    def thirdMax(self, nums):
        n=len(nums)
        i=0
        first=None
        second=None
        third=None
        if n==1:
            return nums[0]
        if n==2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]

        else:
       
        
            
            for i in range(n):
                if nums[i]>first or i==0:
                    third=second
                    second=first
                    first=nums[i]
                if nums[i]<first and nums[i]>second:
                    third=second
                    second=nums[i]
                if nums[i]<second and nums[i]>third:
                    third=nums[i]

                
            if third==None:
                third=first            
                
            return third



        