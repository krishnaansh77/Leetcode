class Solution(object):
    def validMountainArray(self, arr):
        n=len(arr)
        i=0

        #climbing up
        while i<n-1 and arr[i]<arr[i+1]:
            i=i+1

        #check is is only increasing or only decreasing
        if i==0 or i==n-1:
            return False

        #Going down
        while i<n-1 and arr[i]>arr[i+1]:
            i=i+1

        return i==n-1

        