from typing import List


class CanPlaceFlowers(object):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = 0
        counter = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                k += 1
            else:
                k -= 0

            if k >= 2:
                counter += 1
                k = 0

        if counter >= n:
            return True
        return False

    def canPlaceFlowers1(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for i in range(1, len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n -= 1

        return n <= 0



canPlaceFlowers = CanPlaceFlowers()
print(canPlaceFlowers.canPlaceFlowers1([1,0,0,0,1], 1)) #TRUE
print(canPlaceFlowers.canPlaceFlowers1([1,0,0,0,1], 2)) #FALSE
print(canPlaceFlowers.canPlaceFlowers1([1,0,0,0,0,0,1], 2)) #TRUE
print(canPlaceFlowers.canPlaceFlowers1([1,0,0,0,0,1], 2)) # FALSE
print(canPlaceFlowers.canPlaceFlowers1([1,0,0,0,1,0,0], 2)) # TRUE