from typing import List


class FindAllNumbersDisappearedInAnArray:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        valuesDIct = {v: i for i, v in enumerate(nums)}
        res = []
        for n in range(1, len(nums)+1):
            if n in valuesDIct:
                continue
            else:
                res.append(n)
                valuesDIct[n] = n-1
            if len(nums) - len(valuesDIct) == 0:
                break

        return res

    def findDisappearedNumbersOptimalNeet(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            i = abs(n)-1
            nums[i] = -abs(nums[i])

        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)

        return res




driver = FindAllNumbersDisappearedInAnArray()
# print(driver.findDisappearedNumbersOptimalNeet([4,3,2,7,8,2,3,1]))
# print(driver.findDisappearedNumbersOptimalNeet([1, 1]))

print(driver.findDisappearedNumbersOptimalNeet([4,3,2,7,8,2,3,1]))
print(driver.findDisappearedNumbersOptimalNeet([1, 1]))

