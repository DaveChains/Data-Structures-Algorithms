class ValidPalindrome:

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""

        for n in range(len(s)):
            if s[n].isalpha() or s[n].isnumeric() :
                temp += s[n]

        l, r = 0, len(temp)-1
        while l < r:
            if temp[l] != temp[r]:
                return False
            l = l + 1
            r = r - 1
        return True

    def isPalindrome1(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.isAlphaN(s[l]):
                l += 1

            while r > l and not self.isAlphaN(s[r]):
                r -= 1

            sll = s[l].lower()
            srl = s[r].lower()
            if sll != srl:
                return False
            l += 1
            r -= 1

        return True

    def isAlphaN(self, c) -> bool:
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

    def validPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        deleteTimes = 1

        while l < r:
            if s[l] != s[r] and deleteTimes == 1:
                if s[l+1] == s[r] and s[l+2] == s[r-1] and s[l+3] == s[r-2]:
                # s[r-1] != s[l]):
                # and s[l+2] == s[r-1]:
                    deleteTimes -= 1
                    l += 1

            if s[r] != s[l] and deleteTimes == 1:
                if s[r-1] == s[l] and s[r-2] == s[l+1] and s[r-3] == s[l+2]:
                    deleteTimes -= 1
                    r -= 1


            sl, sr = s[l], s[r]
            if sl != sr:
                return False

            l += 1
            r -= 1

        return True


# s1 = "A man, a plan, a canal: Panama"
# s1 = " "
# s1 = ".,"
# s1 = "cbbcc"
# s1 = "abc"
s1 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
s1 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

# s1 = "ebcbb e   c   e   cabba   c   e    c bbcbe"
#             l  l+1 l+2         r-2  r-1  r

s1 = "ebcbbececabbacecbbcbe"

driver = ValidPalindrome()
print(driver.validPalindrome2(s1))
