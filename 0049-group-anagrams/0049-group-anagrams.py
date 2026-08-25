class Solution(object):
    def groupAnagrams(self, strs):
        dict = {}

        for word in strs:
           key = "".join(sorted(word))
    
           if key not in dict:
             dict[key] = []
    
           dict[key].append(word)

        return list(dict.values())