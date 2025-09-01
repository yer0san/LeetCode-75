# difficulty: medium

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        
        area = 0
        while l < r:
            low = min(height[l], height[r])
            width = r - l 
            a = low * width
            if a > area:
                area = a
            if height[l] <= height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return area
            
