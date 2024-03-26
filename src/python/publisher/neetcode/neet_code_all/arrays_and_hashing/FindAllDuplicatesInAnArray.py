from typing import List


class FindAllDuplicatesInAnArray:

    def findAllDuplicatesInAnArray(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            i = abs(n) - 1
            if nums[i] < 0:
                res.append(abs(n))
            nums[i] = -1 * abs(nums[i])

        return res


driver = FindAllDuplicatesInAnArray()
print(driver.findAllDuplicatesInAnArray(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
print(driver.findAllDuplicatesInAnArray(nums=[1, 1, 2]))
