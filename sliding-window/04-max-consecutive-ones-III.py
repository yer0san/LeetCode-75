# difficulty : medium
# couldn't come up with the solution idea

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = max_w = num_zeros = 0

        for i, num in enumerate(nums):
            if num == 1:
                max_w = max(max_w, (i-l+1))
            else:
                num_zeros += 1
                while num_zeros > k and l < len(nums):
                    if nums[l] == 0:
                        num_zeros -= 1
                    l += 1
                max_w = max(max_w, (i-l+1))
        return max_w
