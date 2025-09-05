# difficulty : easy
# time taken : 4:49
# would've been faster to use hashmaps tho

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set(arr)
        resLis = []
        for num in s:
            resLis.append(arr.count(num))
        resSet = set(resLis)
        return len(resLis) == len(resSet)
