# difficulty : easy
# time taken : 5:22


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        answer = []
        ans = []
        for num in s1:
            if num not in s2:
                ans.append(num)
        answer.append(ans)
        ans = []
        for num in s2:
            if num not in s1:
                ans.append(num)
        answer.append(ans)
        return answer
