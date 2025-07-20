difficulty: medium
topics: Array, prefix sum

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = False
        count = 0
        for n in nums:
            if n == 0:
                zeros = True
                count += 1
                if count > 1:
                    zeros = False
                if not zeros:
                    product *= n
                continue
            product *= n
        res = []
        for n in nums:
            if n != 0:
                if zeros:
                    res.append(0)
                else:
                    res.append(product//n)
            else:
                if zeros:
                    res.append(product)
                else:
                    res.append(0)
        return res
                
