# difficulty : medium
# time taken : 35:17

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for ast in asteroids:
            while res and ast < 0 < res[-1]:
                if -ast > res[-1]:
                    res.pop()
                    continue
                elif -ast == res[-1]:
                    res.pop()
                break
            else:
                res.append(ast)

        return res
