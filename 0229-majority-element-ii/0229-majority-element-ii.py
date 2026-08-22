class Solution(object):
    def majorityElement(self, nums):
        length=len(nums)
        d={}
        ans=set()
        
        for x in nums:
            if x not in d:
                d[x]=0
            d[x]=d[x]+1

            if d[x]>(length//3):
                ans.add(x)
        
        return list(ans)      
                
                
              
    
       

           
          
          

       
        