# difficulty : easy
# was not easy at all, alot of edge cases


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        l = 0 
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if flowerbed[l] == 1 and l == 0 and i == 0:
                    continue
                if flowerbed[l] == 0:
                    n -= ((i - l)//2)
                else:
                    n -= ((i - l)//2)-1
                l = i
            
        
        if flowerbed[len(flowerbed)-1] == 0:
            if flowerbed[l] == 0:
                n -= (((len(flowerbed)-1) - l)//2)+1
            else:
                n -= ((len(flowerbed)-1) - l)//2 
        
        return (n <= 0)
