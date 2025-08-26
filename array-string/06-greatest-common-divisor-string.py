# difficulty : easy, lol not easy at all 
# used euclid's algorithm

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 != str2 + str1):
            return ""

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        return str1[:gcd(len(str1), len(str2))]
