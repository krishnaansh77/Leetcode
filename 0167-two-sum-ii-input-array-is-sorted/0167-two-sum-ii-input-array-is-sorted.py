class Solution(object):
    def twoSum(self, numbers, target):
     n=len(numbers)
     ans=[]
     left=0
     right=n-1
     while left<right:
        if numbers[left]+numbers[right]==target:
            ans.append(left+1)
            ans.append(right+1)
            return ans
        elif numbers[left]+numbers[right]<target:
            left+=1
        elif numbers[left]+numbers[right]>target:
            right-=1

