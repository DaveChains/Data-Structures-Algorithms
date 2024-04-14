from typing import List


class RemoveDuplicatesFromSortedArray:

    def removeDuplicatesFromSortedArray(self, nums: List[int]) -> int:
        l = 1
        r = 1

        while r < len(nums):

            right_n = nums[r]
            right_temp = nums[r-1]

            if right_temp != right_n:
                nums[l] = nums[r]

                l+=1
            r+=1

        print(nums)
        return l



driver = RemoveDuplicatesFromSortedArray()
print(driver.removeDuplicatesFromSortedArray([1,1,2]))
print(driver.removeDuplicatesFromSortedArray([0,0,1,1,1,2,2,3,3,4]))