from typing import List


#Time Complexity
class ContainsDuplicate(object):

    def __init__(self):
        pass

    def has_duplicate(self, array):
        temp = {}
        for element in array:
            if temp.get(element) is not None:
                temp.update({element: temp[element]+1})
                return True
            else:
                temp[element] = 1

        return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for n in nums:
            if n in temp:
                return True

            temp.add(n)

        return False


has_dup = ContainsDuplicate()
print(has_dup.has_duplicate([1, 2, 3, 1]))
print(has_dup.has_duplicate([1, 2, 3]))

print(has_dup.containsDuplicate([1, 2, 3, 1]))
print(has_dup.containsDuplicate([1, 2, 3]))
