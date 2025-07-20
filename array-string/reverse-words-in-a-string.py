# difficulty: medium
# topics: two pointers, string

class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split()
        l = 0 
        r = len(lis)-1
        while l < r:
            lis[l], lis[r] = lis[r], lis[l]
            l += 1
            r -= 1
        return " ".join(lis)
