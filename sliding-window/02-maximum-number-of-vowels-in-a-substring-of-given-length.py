# difficulty : medium
# time taken : 27:01

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0

        l = 0
        r = k

        for letter in s[l:r]:
            if s[l] in vowels:
                res += 1
            l += 1
        count = res
        l = 0
        while r < len(s):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            res = max(res, count)
            #count = res
            l, r = l+1, r+1
        return res

