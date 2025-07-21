#difficulty: easy
#topics: two pointers, strings. I don't think i used two pointers tho

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)

        if len1 == 0:
            return word2
        if len2 == 0:
             return word1
        
        res = ""
        minn = min(len1, len2)
        for i in range(minn):
            res += word1[i]
            res += word2[i]
        
        if len1 > len2:
            res += word1[len2:]
        if len2 > len1:
            res += word2[len1:]
        
        return res
