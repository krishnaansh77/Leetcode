class Solution(object):
    def isSubsequence(self, s, t):
       left=0
       right=0
       while left<len(t) and right<len(s):
        if t[left]==s[right]:
            left+=1
            right+=1
        else:
            left+=1
       if right==len(s):
        return True
       else:
        return False