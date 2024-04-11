class ValidPalindromeII:

    def isPalindrome2(self, s:str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            slChar = s[l]
            srChar = s[r]

            if slChar != srChar:
                slRemain = s[l+1: r+1]
                srRemain = s[l : r]
                return (slRemain == slRemain[::-1] or srRemain == srRemain[::-1])


            l += 1
            r -= 1

        return True

    def validPalindromeII(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            slChar = s[l]
            srChar = s[r]

            if slChar != srChar:
                slRemain = s[l+1: r+1]
                srRemain = s[l : r]
                # return (slRemain == slRemain[::-1] or srRemain == srRemain[::-1])
                # return self.remainsPalindromHelper(s, l+1, r) or self.remainsPalindromHelper(s, l, r-1)
                return self.remainsPalindromHelper(slRemain) or self.remainsPalindromHelper(srRemain)
            l += 1
            r -= 1

        return True

    def remainsPalindromHelper(self, s:str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            skipLL = s[l]
            skipLR = s[r]

            if skipLL != skipLR:
                return False
            l += 1
            r -= 1

        return True


driver = ValidPalindromeII()
print(driver.validPalindromeII("aba")) # True
print(driver.validPalindromeII("abca")) # True
print(driver.validPalindromeII("abc")) # False
print(driver.validPalindromeII("deeee")) # True