from typing import List


class ContainsDuplicateII:

    def containsNearbyDuplicate(self, nums:List[int], k: int)-> bool:
        l = 0
        visitedWindow = set()

        for r in range(len(nums)):

            if len(visitedWindow) == k+1:
                visitedWindow.remove(nums[l])
                l += 1

            if nums[r] in visitedWindow:
                return True

            visitedWindow.add(nums[r])

        return False

driver = ContainsDuplicateII()
print(driver.containsNearbyDuplicate([1,2,3,1], 3)) #true
print(driver.containsNearbyDuplicate([1,0,1,1], 1)) #true
print(driver.containsNearbyDuplicate([1,2,3,1,2,3], 1)) #false
