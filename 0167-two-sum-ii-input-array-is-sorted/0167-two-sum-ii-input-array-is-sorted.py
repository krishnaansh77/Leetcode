class Solution(object):
    def twoSum(self, numbers, target):
        ans=[]
        left=0
        right=len(numbers)
        while left<=right:
            sum=numbers[left]+numbers[right-1]
            if sum==target:
                ans.append(left +1)
                ans.append(right)
                return ans
            elif sum<target:
                left=left+1
            elif sum>target:
                right=right-1

