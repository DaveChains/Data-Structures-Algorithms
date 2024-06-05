from typing import List


class FindAllAnagramsInAString: #438
    def findAllAnagramsInAString(self, s:str, p:str) -> List[int]:
        if len(p) > len(s):
            return []

        sMap = [0] * 26
        pMap = [0] * 26

        for n in range(len(p)):
            pMap[ord(p[n]) - ord("a")] += 1

        l = 0
        res = []
        for r in range(len(s)):

            indexL = ord(s[l]) - ord("a")
            indexR = ord(s[r]) - ord("a")

            while l == r - len(p):
                if sMap[indexL] > 1:
                    sMap[indexL] = sMap[indexL] - 1
                else:
                    sMap[indexL] = 0
                l += 1

            sMap[indexR] += 1
            if sMap == pMap:
                res.append(l)
        return res

    def findAllAnagramsInAStringNeat(self, s: str, p: str):
        if len(p) > len(s):
            return []

        sCount = {}
        pCount = {}

        for c in p:
            pCount[c] = pCount.get(c, 0) + 1

        l = 0
        res = []
        for r in range(len(s)):

            while l == r-len(p):
                if sCount.get(s[l], 0) > 1:
                    sCount[s[l]] = sCount.get(s[l], 0) - 1
                else:
                    sCount.pop(s[l])

                l += 1

            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if pCount == sCount:
                res.append(l)

        return res




driver = FindAllAnagramsInAString()
print(driver.findAllAnagramsInAStringNeat(s="cbaebabacd", p="abc"))
print(driver.findAllAnagramsInAStringNeat(s="abab", p="ab"))