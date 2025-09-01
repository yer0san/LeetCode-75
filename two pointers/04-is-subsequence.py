# difficulty : easy

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if s[p] == t[i]:
                p += 1
            if p == len(s):
                return True
        return False
