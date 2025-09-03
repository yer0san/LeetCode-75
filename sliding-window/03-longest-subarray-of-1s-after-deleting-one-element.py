# difficulty : medium
# time taken : 37:41


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums) - 1
        
        res = 0
        l = 0
        while nums[l] != 0:
            l += 1
        for i,num in enumerate(nums):
            r = 1
            if num == 0:
                while (i+r) < len(nums):
                    if nums[i+r] == 1:
                        r += 1
                    else:
                        break
                res = max(res, l+r-1)
                l = r-1
        return res
