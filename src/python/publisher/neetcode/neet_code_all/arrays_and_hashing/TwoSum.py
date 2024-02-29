from typing import List


class TwoSum():

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
            print[i]
        return

    def two_sum_two_pointers(self, nums, target):
        l_index = 0
        r_index = len(nums) - 1

        # dict_nums = {v : k for k, v in enumerate(nums)}
        aux_nums = [(v, i) for i, v in enumerate(nums)]
        aux_nums.sort()
        # sorted_nums = sorted(nums)
        for i in range(len(nums)):

            s = aux_nums[l_index][0] + aux_nums[r_index][0]

            if s == target:
                return [aux_nums[l_index][1], aux_nums[r_index][1]]

            elif s > target:
                r_index -= 1
            else:
                l_index += 1

    def twe_sum_brute_force(self, nums, target):
        for i, n in enumerate(nums):
            for index in range(1, len(nums)):
                value = nums[index]
                if n + value == target:
                    return [i, index]

    def two_sum_dic(self, nums, target):
        prev = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in prev:
                return [prev[diff], i]
            prev[value] = i


twoSum = TwoSum()

list = twoSum.twoSum(nums=[2, 3, 9, 4, 5, 6], target=7)
print(list)

print(twoSum.two_sum_two_pointers([2, 7, 11, 15], 9))
print(twoSum.two_sum_two_pointers([3, 2, 4], 6))
print(twoSum.two_sum_two_pointers([3, 3], 6))

# print(twoSum.twe_sum_brute_force([2, 7, 11, 15], 9))
# print(twoSum.twe_sum_brute_force([3, 2, 4], 6))
# print(twoSum.twe_sum_brute_force([3, 3], 6))


#
# print(twoSum.two_sum_dic([2, 7, 11, 15], 9))
# print(twoSum.two_sum_dic([3, 3], 6))
# print(twoSum.two_sum_dic([3, 2, 4], 6))