from typing import List
from collections import deque
from queue import LifoQueue


class NextGreaterElement(object):
    def nextGreaterElement(self,  nums1: List[int],  nums2: List[int]) -> List[int]:
        response = []
        index = 0
        greater = 0
        for i in range(len(nums1)):

            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    index = j

                if (nums1[i] == nums2[index]
                        and nums2[j] > nums2[index]
                        and nums2[j] > greater):
                    greater = nums2[j]
                    break
                else:
                    greater = -1
                j += 1
            response.append(greater)

        return response

    def neetNextGreaterElement(self,  nums1: List[int],  nums2: List[int]) -> List[int]:
        nums1_dict = {n: i for i,  n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i,  num2 in enumerate(nums2):
            if num2 in nums1_dict:
                idx = i+1
                while idx < len(nums2):
                    if nums2[idx] > num2:
                        position = nums1_dict[num2]
                        res[position] = nums2[idx]
                        idx = i
                        break
                    idx += 1

        return res

    def neet_with_stackNextGreaterElement(self,  nums1: List[int],  nums2: List[int]) -> List[int]:
        nums1_dict = {n : i for i,  n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = deque()
        for idx in range(len(nums2)):
            current = nums2[idx]

            if len(stack) > 0 and current > stack[0]:
                length = len(stack)
                for i in range(length):
                    num = stack.popleft()
                    num_idx = nums1_dict[num]
                    res[num_idx] = current

            if current in nums1_dict:
                if current not in stack:
                    stack.appendleft(current)
        return res

    def neet2_with_stack_nextGreaterElement(self,  nums1: List[int],  nums2: List[int])-> List[int]:
        nums1_dict = {n:i for i,  n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        stackd = deque()
        for i in range(len(nums2)):
            current = nums2[i]

            while len(stackd) > 0 and current > stackd[-1]:
                num = stackd.pop()
                idx = nums1_dict[num]
                res[idx] = current
            if current in nums1_dict:
                stackd.append(current)

        return res


nge = NextGreaterElement()
print(nge.neet2_with_stack_nextGreaterElement([4, 1, 2],  [2,  1,  3,  4]))
print(nge.neet2_with_stack_nextGreaterElement([2,  1,  3,  4],  [2,  1,  3,  4]))
# print(nge.neet2_with_stack_nextGreaterElement([4, 1, 2],  [1,  3,  4,  2]))
# print(nge.neet2_with_stack_nextGreaterElement([4, 1, 2],  [1,  2,  3,  4]))
# print(nge.neet2_with_stack_nextGreaterElement([2,  4],  [1,  2,  3,  4]))
# print(nge.neet2_with_stack_nextGreaterElement([1, 3, 5, 2, 4],  [6, 5, 4, 3, 2, 1, 7]))
print(nge.neet2_with_stack_nextGreaterElement([137, 59, 92, 122, 52, 131, 79, 236, 94, 171, 141, 86, 169, 199, 248, 120, 196, 168, 77, 71, 
                                               5, 198, 215, 230, 176, 87, 189, 206, 115, 76, 13, 216, 197, 26, 183, 54, 250, 27, 109, 140, 
                                               147, 25, 96, 105, 30, 207, 241, 8, 217, 40, 0, 35, 221, 191, 83, 132, 9, 144, 12, 91, 175, 65, 
                                               170, 149, 174, 82, 102, 167, 62, 70, 44, 143, 10, 153, 160, 142, 188, 81, 146, 212, 15, 162, 
                                               103, 163, 123, 48, 245, 116, 192, 14, 211, 126, 63, 180, 88, 155, 224, 148, 134, 158, 119, 
                                               165, 130, 112, 166, 93, 125, 1, 11, 208, 150, 100, 106, 194, 124, 2, 184, 75, 113, 104, 18, 
                                               210, 202, 111, 84, 223, 173, 238, 41, 33, 154, 47, 244, 232, 249, 60, 164, 227, 253, 56, 157, 
                                               99, 179, 6, 203, 110, 127, 152, 252, 55, 185, 73, 67, 219, 22, 156, 118, 234, 37, 193, 90, 
                                               187, 181, 23, 220, 72, 255, 58, 204, 7, 107, 239, 42, 139, 159, 95, 45, 242, 145, 172, 209, 
                                               121, 24, 21, 218, 246, 49, 46, 243, 178, 64, 161, 117, 20, 214, 17, 114, 69, 182, 85, 229, 
                                               32, 129, 29, 226, 136, 39, 36, 233, 43, 240, 254, 57, 251, 78, 51, 195, 98, 205, 108, 61, 66, 
                                               16, 213, 19, 68, 237, 190, 3, 200, 133, 80, 177, 97, 74, 138, 38, 235, 135, 186, 89, 201, 4, 
                                               101, 151, 31, 228, 231, 34, 225, 28, 222, 128, 53, 50, 247], 
                                              [137, 59, 92, 122, 52, 131, 79, 236, 94, 171, 141, 86, 169, 199, 248, 120, 196, 168, 77, 71, 
                                               5, 198, 215, 230, 176, 87, 189, 206, 115, 76, 13, 216, 197, 26, 183, 54, 250, 27, 109, 140, 
                                               147, 25, 96, 105, 30, 207, 241, 8, 217, 40, 0, 35, 221, 191, 83, 132, 9, 144, 12, 91, 175, 65, 
                                               170, 149, 174, 82, 102, 167, 62, 70, 44, 143, 10, 153, 160, 142, 188, 81, 146, 212, 15, 162, 
                                               103, 163, 123, 48, 245, 116, 192, 14, 211, 126, 63, 180, 88, 155, 224, 148, 134, 158, 119, 
                                               165, 130, 112, 166, 93, 125, 1, 11, 208, 150, 100, 106, 194, 124, 2, 184, 75, 113, 104, 18, 
                                               210, 202, 111, 84, 223, 173, 238, 41, 33, 154, 47, 244, 232, 249, 60, 164, 227, 253, 56, 157, 
                                               99, 179, 6, 203, 110, 127, 152, 252, 55, 185, 73, 67, 219, 22, 156, 118, 234, 37, 193, 90, 187, 
                                               181, 23, 220, 72, 255, 58, 204, 7, 107, 239, 42, 139, 159, 95, 45, 242, 145, 172, 209, 121, 24, 
                                               21, 218, 246, 49, 46, 243, 178, 64, 161, 117, 20, 214, 17, 114, 69, 182, 85, 229, 32, 129, 29, 
                                               226, 136, 39, 36, 233, 43, 240, 254, 57, 251, 78, 51, 195, 98, 205, 108, 61, 66, 16, 213, 19, 
                                               68, 237, 190, 3, 200, 133, 80, 177, 97, 74, 138, 38, 235, 135, 186, 89, 201, 4, 101, 151, 31, 228, 231, 34, 225, 28, 222, 128, 53, 50, 247]))
print("[236, 92, 122, 131, 131, 236, 236, 248, 171, 199, 169, 169, 199, 248, 250, 196, 198, 198, 198, 198, 198, 215, 230, 250, 189, 189, 206, 216, 216, 216, 216, 250, 250, 183, 250, 250, 253, 109, 140, 147, 207, 96, 105, 207, 207, 241, 245, 217, 221, 221, 35, 221, 245, 212, 132, 144, 144, 175, 91, 175, 188, 170, 174, 174, 188, 102, 167, 188, 70, 143, 143, 153, 153, 160, 188, 188, 212, 146, 212, 245, 162, 163, 163, 245, 245, 245, 249, 192, 211, 211, 224, 180, 180, 224, 155, 224, 238, 158, 158, 165, 165, 166, 166, 166, 208, 125, 208, 11, 208, 210, 194, 106, 194, 210, 184, 184, 210, 113, 210, 210, 210, 223, 223, 223, 223, 238, 238, 244, 154, 154, 244, 244, 249, 249, 253, 164, 227, 253, 255, 157, 179, 179, 203, 203, 252, 127, 152, 252, 255, 185, 219, 219, 219, 234, 156, 234, 234, 255, 193, 220, 187, 220, 220, 220, 255, 255, -1, 204, 239, 107, 239, 242, 139, 159, 242, 242, 242, 246, 172, 209, 218, 218, 218, 218, 246, 254, 243, 243, 254, 214, 161, 214, 214, 214, 229, 114, 182, 182, 229, 229, 233, 129, 226, 226, 233, 233, 233, 233, 240, 240, 254, -1, 251, -1, 195, 195, 205, 205, 213, 213, 66, 213, 213, 237, 68, 237, 247, 200, 200, 235, 177, 177, 235, 138, 138, 235, 235, 247, 186, 201, 201, 228, 101, 151, 228, 228, 231, 247, 225, 247, 222, 247, 247, 247, 247, -1]")