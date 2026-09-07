class Solution(object):
    def canConstruct(self, ransomNote, magazine):
       mag={}

       for x in magazine:
        mag[x]=mag.get(x,0)+1

       for y in ransomNote:
        if y not in mag or mag[y]<1:
            return False
        mag[y]-=1
       return True