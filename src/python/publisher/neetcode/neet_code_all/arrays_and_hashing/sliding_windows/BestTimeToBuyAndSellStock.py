from typing import List


class BestTimeToBuyAndSellStock:

    def getBestTimeToBuyAndSellStock(self, prices: List[int]) -> int:

        l = 0
        max_profit = 0
        for r in range(len(prices)):
            current = prices[r] - prices[l]
            if current > max_profit:
                max_profit = current

            if prices[r] < prices[l]:
                l = r
            r += 1

        return max_profit


driver = BestTimeToBuyAndSellStock()
print(driver.getBestTimeToBuyAndSellStock([7, 1, 5, 3, 6, 4]))
print(driver.getBestTimeToBuyAndSellStock([7,6,4,3,1]))
