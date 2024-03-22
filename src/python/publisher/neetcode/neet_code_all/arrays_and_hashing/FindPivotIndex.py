from typing import List


class FindPivotIndex(object):
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums: total += n

        l_sum_temp = 0
        nums_temp = [0] + nums
        res = -1
        for i in range(len(nums)):
            l_sum_temp = l_sum_temp + nums_temp[i]
            r_sum_temp = total - l_sum_temp - nums[i]
            if l_sum_temp == r_sum_temp: # if I find it Idont need to keep iterating
                return i

        return res

    def findPivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums: total += n
        l_sum_temp = 0

        for i in range(len(nums)):
            r_sum_temp = total - l_sum_temp - nums[i]
            if l_sum_temp == r_sum_temp:
                return i

            l_sum_temp += nums[i]

        return -1




driver = FindPivotIndex()
print(driver.findPivotIndex([1, 7, 3, 6, 5, 6])) # total = 28 result = 3
print(driver.findPivotIndex([1, 2, 3])) # total = 6 result = -1
print(driver.pivotIndex([2, 1, -1])) # total = 2 # result = 0
