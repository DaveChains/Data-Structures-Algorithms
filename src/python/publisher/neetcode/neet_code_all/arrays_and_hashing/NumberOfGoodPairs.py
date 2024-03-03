from collections import Counter
from typing import List


class NumberOfGoodPairs(object):
    def easy_getGoodPair(self, nums: List[int])-> int:
        res = 0
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
                res += count[n] - 1

            else:
                count[n] = 1

        return res

    def getGoodPair(self, nums:[]) -> int:
        count = 0
        index_l = 0
        index_r = 1
        while index_l < len(nums)-1:
            if nums[index_l] == nums[index_r]:
                count += 1

            if index_r == len(nums)-1:
                index_l += 1
                index_r = index_l+1
            else:
                index_r += 1

        return count

    def neet_long_getGoodPair(self, nums:[]) -> int:
        counter = {}
        result = 0
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        for i, c in enumerate(counter):

            result += counter[c] * (counter[c] - 1) / 2  # c == coutn * count -1 / 2

        return int(result)

    def neet_getGoodPair(self, nums):
        count = Counter(nums)
        res = 0
        for n, c in count.items():
            res += c * c-1 // 2
        return res


numbers = NumberOfGoodPairs()

# print(numbers.getGoodPair([1, 2, 3, 1, 1, 3]))
# print(numbers.getGoodPair([1, 1, 1, 1]))

# print(numbers.neet_getGoodPair([1, 2, 3, 1, 1, 3]))
# print(numbers.neet_getGoodPair([1, 1, 1, 1]))

print(numbers.easy_getGoodPair([1, 2, 3, 1, 1, 3]))
print(numbers.easy_getGoodPair([1, 1, 1, 1]))



