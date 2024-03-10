from typing import List


class PascalsTriangle(object):
    def buildPascalsTriangle(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1 ):

                row.append(temp[j] + temp[j+1])
            res.append(row)

        return res


pascalsTriangle = PascalsTriangle()
print(pascalsTriangle.buildPascalsTriangle(5))
print(pascalsTriangle.buildPascalsTriangle(0))