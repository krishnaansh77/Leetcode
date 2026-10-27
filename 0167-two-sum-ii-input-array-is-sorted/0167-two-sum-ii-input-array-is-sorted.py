class Solution(object):
    def twoSum(self, numbers, target):
        n=len(numbers)
        left=0
        right=n-1
        res=[]
        while left<right:
          total=numbers[left]+numbers[right]
          if total==target:
            res.append(left+1)
            res.append(right+1)
            return res
          elif total<target:
            left+=1
          else:
            right-=1
    


  