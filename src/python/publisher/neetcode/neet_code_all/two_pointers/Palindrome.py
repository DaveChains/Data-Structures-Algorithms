class Palindrome(object):
    def isPalindrome(self, s):
        s_lower = s.lower()
        alpha_s = [c for c in s_lower if c.isalpha()]
        print(alpha_s)
        l = 0
        r = len(alpha_s) - 1
        while l < r:
            if alpha_s[l] != alpha_s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True

    def isPalindrome2(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalpha():
                 l += 1

            while not s[r].isalpha():
                 r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True




palin = Palindrome()

# Transforming string and getting just the list of characters as alphas
# print(palin.isPalindrome("A man, a plan, a canal: Panama"))
# print(palin.isPalindrome("race a car"))
# print(palin.isPalindrome(" "))


# two pointers - # each while loop moves R and L as they find a non alpha character
print(palin.isPalindrome2("A man, a plan, a canal: Panama"))
print(palin.isPalindrome2("race a car"))
print(palin.isPalindrome2(" "))
