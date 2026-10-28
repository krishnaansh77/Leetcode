class Solution(object):
    def removeDuplicates(self, nums):
       left=0
       right=0
       
       while right<len(nums):
        if nums[right]!=nums[left]:
            nums[left+1]=nums[right]
            left+=1
            
        
    
        right+=1
       return left+1


          
        


        