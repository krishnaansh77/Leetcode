class Solution(object):
    def runningSum(self, nums):
        arr=[]
        sum=0
        for x in nums:
            sum=sum+x
            arr.append(sum)
        return arr

        