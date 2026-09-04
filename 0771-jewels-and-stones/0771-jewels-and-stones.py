class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels=set(jewels)
        count=0
        for x in stones:
            if x in jewels:
                count+=1
        return count
        