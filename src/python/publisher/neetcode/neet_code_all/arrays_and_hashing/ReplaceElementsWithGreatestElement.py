from typing import List


class ReplaceElementsWithGreatestElement(object):

    def replaceElements(self, arr: List[int]) -> List[int]:
    # initial max -1
    # replace element
    # loop in reverse
        startR = -1
        for i in range(len(arr)-1, -1, -1):
            max_val = max(arr[i], startR)
            arr[i] = startR
            startR = max_val


        return arr

    def replaceElementsBF(self, arr: List[int]) -> List[int]:

        for i, value_l in enumerate(arr):
            for i_r, value_r in enumerate(arr, start=i+1):
                print(value_l, " ", value_r )

        return arr

replace = ReplaceElementsWithGreatestElement()

# print(replace.replaceElements([17, 18, 5, 4, 6, 1])) # -1
print(replace.replaceElementsBF([17, 18, 5, 4, 6, 1])) # -1