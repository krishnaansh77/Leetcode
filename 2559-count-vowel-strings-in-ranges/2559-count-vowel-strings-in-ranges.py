class Solution(object):
    def vowelStrings(self, words, queries):
        n=len(words)
        prefix=[0]*n
        vowels="aeiou"
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i]=1
            if i>0:
                prefix[i]+=prefix[i-1]
            

        ans=[]
        for l,r in queries:
            if l==0:
                ans.append(prefix[r])
            
            else:
                ans.append(prefix[r]-prefix[l-1])

        return ans
            

        