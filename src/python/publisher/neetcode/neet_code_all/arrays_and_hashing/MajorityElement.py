import math
from typing import List

class MajorityElement(object):

    def majorityElement(self, nums: List[int]) -> int:
                        #Total, counts/2
        count = {"highest": (0, 0.0)}

        for num in nums:
            current = 0
            if num in count:
                counts = count[num][0] + 1
                average = counts / 2
                count[num] = (counts, average)
                current = average
            else:
                average = 1 #1 / 2
                count[num] = (1, average)
                current = average

            if current > count["highest"][1]:
                count["highest"] = (num, current)

        return count["highest"][0]

    def majorityFormula(self, num):
        return num / 2

    def neetMajorityElement(self, nums: List[int]) -> int:
        count = {}
        res = 0
        maxCount = 0
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > maxCount:
                res = n
                maxCount = count[n]
        return res

    def neetOptimizedMajorityElement(self, nums: List[int]) -> int:

        res = 0
        maxCount = 0
        for n in nums:
            if maxCount == 0:
                res = n
            if n == res:
                maxCount += 1
            else: maxCount -= 1
        return res



majorityElement = MajorityElement()

# print(majorityElement.majorityElement([3,2,3]))
# print(majorityElement.majorityElement([2,2,1,1,1,2,2]))
# print(majorityElement.majorityElement([6,5,5]))
# print(majorityElement.majorityElement([1,1,1,1,1,1,8]))


# print(majorityElement.neetMajorityElement([3,2,3]))
# print(majorityElement.neetMajorityElement([2,2,1,1,1,2,2]))
# print(majorityElement.neetMajorityElement([6,5,5]))
# print(majorityElement.neetMajorityElement([1,1,1,1,1,1,8]))


print(majorityElement.neetOptimizedMajorityElement([3,2,3]))
print(majorityElement.neetOptimizedMajorityElement([2,2,1,1,1,2,2]))
print(majorityElement.neetOptimizedMajorityElement([6,5,5]))
print(majorityElement.neetOptimizedMajorityElement([1,1,1,1,1,1,8]))