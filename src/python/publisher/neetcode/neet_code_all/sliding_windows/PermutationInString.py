

class PermutationInString:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        s2Map = {}
        for n in range(len(s1)):
            s1Map[s1[n]] = s1Map.get(s1[n], 0) + 1

        l = 0
        for r in range(len(s2)):

            while l == r-len(s1):
                if s2Map[s2[l]] > 1:
                    s2Map[s2[l]] = s2Map.get(s2[l], 0) - 1
                else:
                    s2Map.pop(s2[l])
                l += 1
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            if s1Map == s2Map:
                return True

        return False

    def checkInstancesArray(self, s1: str, s2: str):
        if len(s1) > len(s2): return False
        s1Map = [0] * 26
        s2Map = [0] * 26

        for c in range(len(s1)):
            s1Map[ord(s1[c]) - ord("a")] += 1
            # s2Map[ord(s2[c]) - ord("a")] += 1

        l = 0
        for r in range(len(s2)):
            indexL = ord(s2[l]) - ord("a")
            indexR = ord(s2[r]) - ord("a")

            while l == r-len(s1):
                if s2Map[indexL] > 1:
                    s2Map[indexL] = s2Map[indexL] - 1
                else:
                    s2Map[indexL] = 0
                l += 1

            s2Map[indexR] += 1

            if s1Map == s2Map:
                return True
        return False

    def checkInclusionNeat(self, s1: str, s2: str) -> bool:
            if len(s1) > len(s2):
                return False

            s1Count, s2Count = [0] * 26, [0] * 26
            for i in range(len(s1)):
                s1Count[ord(s1[i]) - ord("a")] += 1
                s2Count[ord(s2[i]) - ord("a")] += 1

            matches = 0
            for i in range(26):
                matches += 1 if s1Count[i] == s2Count[i] else 0

            l = 0
            for r in range(len(s1), len(s2)):
                if matches == 26:
                    return True

                index = ord(s2[r]) - ord("a")
                s2Count[index] += 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] + 1 == s2Count[index]:
                    matches -= 1

                index = ord(s2[l]) - ord("a")
                s2Count[index] -= 1
                if s1Count[index] == s2Count[index]:
                    matches += 1
                elif s1Count[index] - 1 == s2Count[index]:
                    matches -= 1
                l += 1
            return matches == 26


driver = PermutationInString()

print(driver.checkInclusionNeat("ab", "aidbaooo"))
print(driver.checkInclusion("ab", "eidboaoo"))
print(driver.checkInclusion("a", "ab"))
print(driver.checkInclusion("adc", "dcda"))

