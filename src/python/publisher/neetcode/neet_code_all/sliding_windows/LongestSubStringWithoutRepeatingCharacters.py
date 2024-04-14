class LongestSubStringWithoutRepeatingCharacters:

    def lengthOfLongestSubstring2(self, s: str) -> int:

        l = 0
        window = set()
        counter = 0
        maxCounter = 0

        for r in range(len(s)):

            if s[r] in window:
                maxCounter = counter if counter > maxCounter else maxCounter
                counter = 0
                window = set()
            window.add(s[r])
            counter += 1

        return counter if counter > maxCounter else maxCounter

    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        window = set()
        maxCounter = 0

        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l+=1

            window.add(s[r])

            maxCounter = max(maxCounter, r - l+1)

        return maxCounter


driver = LongestSubStringWithoutRepeatingCharacters()
print(driver.lengthOfLongestSubstring("abcabcbb"))
print(driver.lengthOfLongestSubstring("bbbbb"))
print(driver.lengthOfLongestSubstring("pwwkew"))
print(driver.lengthOfLongestSubstring(" "))
print(driver.lengthOfLongestSubstring("au"))
print(driver.lengthOfLongestSubstring("dvdf"))