# -- Brute Force --
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l = len(flowerbed)
        for i in range(0, l): 
            if flowerbed[i] == 1: 
                continue
            else:
                if l == 1 or n == 0:
                    return True
                elif i == 0 and flowerbed[i+1] == 0:
                    n = n - 1
                    flowerbed[i] = 1
                elif i == l-1 and flowerbed[i-1] == 0: 
                    n = n - 1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n = n - 1
                    flowerbed[i] = 1
        return n == 0
