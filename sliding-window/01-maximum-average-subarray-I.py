# difficulty : easy

# time taken : 5:00

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k
        s = sum(nums[l:r])
        res = s/k
        while r < len(nums):
            s = s - nums[l] + nums[r]
            res = max(res, s/k)
            l, r = l+1, r+1
        return res

        
