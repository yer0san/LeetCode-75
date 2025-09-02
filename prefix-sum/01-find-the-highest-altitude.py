# difficulty : easy
# time taken : 8:02

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        s = 0
        for alt in gain:
            s += alt
            res = max(s, res)
        return res
