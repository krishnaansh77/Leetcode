class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        A={}
        B={}
        for x,y in zip(s,t):
            A[x]=A.get(x,0)+1
            B[y]=B.get(y,0)+1
        for p,q in zip(A,B):
            if p not in B or A[p]!=B[p]:
                return False
            if q not in A or B[q]!=A[q]:
                return False
        return True
        