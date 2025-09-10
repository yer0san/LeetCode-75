# difficulty : medium
# had to look up the best way to do this and damn, this answer is just beautiful 

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = s = max(nums)
        
        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else:
                return True
        return False
