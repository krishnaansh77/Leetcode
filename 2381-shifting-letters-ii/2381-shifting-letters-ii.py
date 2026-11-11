class Solution(object):
    def shiftingLetters(self, s, shifts):
        n=len(s)
        diff=[0]*(n+1)

        for first,last,direction in shifts:
            if direction==0:
                action=-1
            else:
                action=1
            diff[first]+=action
            diff[last+1]-=action

        total=0
        ans=[]

        for i in range(n):
            total+=diff[i]
            ans.append(chr((ord(s[i])+total-97)%26+97))

        return''.join(ans)

        