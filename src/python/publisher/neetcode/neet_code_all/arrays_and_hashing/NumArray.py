from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.isSumProcessed = {}
        self.preProcess = [0]
        total = 0
        for n in range(len(nums)):
            total = total + self.nums[n]
            self.preProcess.append(total)

    def sumRange(self, left: int, right: int) -> int:
        isComputed = self.preProcess.get((left, right), 0)
        if isComputed != 0:
            return isComputed

        total = 0
        for n in range(left, right+1):
            temp = (total, self.nums[n])
            total = sum(temp)
            self.isSumProcessed[(left, right)] = total

        return total

    def sumRange2(self, left: int, right: int) -> int:
        l = self.preProcess[left] if self.preProcess[left] else 0
        return self.preProcess[right] - l




#
# ["NumArray","sumRange","sumRange","sumRange"]
# [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]
driver = NumArray([-2,0,3,-5,2,-1])
#
print(driver.sumRangeNeet(0, 2))
print(driver.sumRangeNeet(2, 5))
print(driver.sumRangeNeet(0, 5))
print(driver.preProcess)

# driver = NumArray([-4,-5])
# print(driver.sumRange(0, 0))
# print(driver.sumRange(1, 1))
# print(driver.sumRange(0, 1))
# print(driver.sumRange(1, 1))
# print(driver.sumRange(0, 0))