import math
from typing import List


class SignProductOfArray: # 1822

    def arraySign(self, nums: List[int]) -> int:
        product = 0

        product = math.prod(nums)

        return self.signFunc(product)

    def signFunc(self, product) -> int:
        if product > 0:
            return 1
        elif product < 0:
            return -1
        elif product == 0:
            return 0


driver = SingProductOfArray()
print(driver.arraySign(nums=[-1,-2,-3,-4,3,2,1]))
print(driver.arraySign(nums=[1,5,0,2,-3]))
print(driver.arraySign(nums=[-1,1,-1,1,-1]))