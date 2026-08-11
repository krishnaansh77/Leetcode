class Solution(object):
    def lengthOfLastWord(self, s):
        arr=s.split()
        n=len(arr)
        return len(arr[n-1])
        