from typing import List


class FrequencyOfTheMostFrequentElement(): #1838

    def maxFrequencyOfTheMostFrequentElement(self, nums: List, k: int) -> int:
        nums.sort()
        l, r = 0, 0
        res, total = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1

            newWL = (r - l + 1)
            res = max(res, newWL)
            r += 1

        return res


driver = FrequencyOfTheMostFrequentElement()
print(driver.maxFrequencyOfTheMostFrequentElement([1,2,4], 5)) # == 3
print(driver.maxFrequencyOfTheMostFrequentElement([1, 4, 8, 13], 5)) # == 2
print(driver.maxFrequencyOfTheMostFrequentElement([3,9,6], 2)) # == 1