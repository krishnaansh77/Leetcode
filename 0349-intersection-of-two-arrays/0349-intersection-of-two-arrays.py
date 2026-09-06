class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=set(nums1)
        nums2=set(nums2)
        arr=[]
        for x in nums1:
            if x in nums2:
                arr.append(x)
        return arr