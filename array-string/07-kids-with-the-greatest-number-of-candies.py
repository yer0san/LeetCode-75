# difficulty : easy
# don't mind the extra space used for s :)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        s = candies[:]
        s.sort()
        
        result = []
        for num in candies:
            if num + extraCandies >= s[-1]:
                result.append(True)
            else:
                result.append(False)

        return result
