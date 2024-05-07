from typing import List


class TopKFrequentElements:
    def TopKFrequentElements(self, nums: List[int], k: int):
        count = {}
        arr = [[]] * (len(nums) + 1)
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, value in zip(count.keys(), count.values()):
            arr[value] = arr[value] + [key]

        for r in range(len(arr)-1, 0, -1):
            while len(arr[r]) > 0 and k > 0:
                res.append(arr[r].pop())
                k-=1

            if k == 0:
                break

        return res




driver = TopKFrequentElements()
print(driver.TopKFrequentElements([1,1,1,2,2, 3], 2)) #[1,2]
print(driver.TopKFrequentElements([1], 1)) # [1]
print(driver.TopKFrequentElements([1, 2], 2)) #[1,2]
print(driver.TopKFrequentElements([4,1,-1,2,-1,2,3], 2)) #[2,-1]