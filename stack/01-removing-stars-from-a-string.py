# difficulty : medium
# time taken : 15:41

class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for r in range(len(s)):
            if s[r] != '*':
                res.append(s[r])
            else:
                res.pop()
        return "".join(res)
