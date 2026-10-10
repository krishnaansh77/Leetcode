class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        right=0
        t=""
        while left<len(word1) or right<len(word2):
            if left!=len(word1):
                t += word1[left]
                left+=1
            if right!=len(word2):
                t +=word2[right]
                right+=1

        return t


        