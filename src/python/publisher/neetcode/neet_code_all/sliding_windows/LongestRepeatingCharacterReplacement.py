class LongestRepeatingCharacterReplacement:
    def longestRepeatingCharacterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            if r - l +1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

        return res

driver = LongestRepeatingCharacterReplacement()
print(driver.longestRepeatingCharacterReplacement("ABAB", 2))
print(driver.longestRepeatingCharacterReplacement("AABABBA", 1))
