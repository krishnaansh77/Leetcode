class Solution(object):
    def maximumWealth(self, accounts):
        new_max=0
        max=0
        for i in accounts:
            new_max=sum(i)
            if new_max>max:
                max=new_max
        return max
            
        