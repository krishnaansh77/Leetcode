class Solution(object):
    def removeDuplicates(self, nums):
       left=0
       right=0
       k=1
       while right<len(nums):
        if nums[left]!=nums[right]:
            nums[left+1]=nums[right]
            left+=1
            k+=1
        
            
            
        right+=1
       return k

          
        


        