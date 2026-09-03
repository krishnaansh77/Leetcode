class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count=0
        map={}
        for x in nums1:
            for y in nums2:
                target=x+y
                map[target]=map.get(target,0)+1

        for m in nums3:
            for n in nums4:
                need=-(m+n)
                if need in map:
                    count+=map[need]
        return count

        