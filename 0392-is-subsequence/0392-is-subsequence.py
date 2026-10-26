class Solution(object):
    def isSubsequence(self, s, t):
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        left=0
        right=0
        while right<len(t):
            if s[left]==t[right]:
                left+=1
                if left==len(s):
                    return True
            right+=1
        
        return False
       
       
       
        