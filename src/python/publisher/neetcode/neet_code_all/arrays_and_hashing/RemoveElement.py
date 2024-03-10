from typing import List


class RemoveElement(object):

    def neetRemoveElement(self, nums: List[int], val: int) -> int :
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    def removeElement(self, nums: List[int], val: int)-> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k



rm = RemoveElement()
print(rm.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
print(rm.removeElement([3,2,2,3], 2))
print(rm.removeElement([3,2,2,3], 3))
