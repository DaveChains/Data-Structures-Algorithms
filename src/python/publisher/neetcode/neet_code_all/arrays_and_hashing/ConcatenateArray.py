from typing import List


class ConcatenateArray(object):
    def getConcatenate(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums

    def getConcatenate2(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            result.append(nums[i])

        for n in range(len(result)):
            result.append(nums[n])

        return result


concat = ConcatenateArray()

# print(concat.getConcatenate([1, 2, 1]))
print(concat.getConcatenate2([1, 2, 1]))
print(concat.getConcatenate2([1,3,2,1]))
