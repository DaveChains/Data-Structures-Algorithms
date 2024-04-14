from typing import List


class ReverseString:

    def reverseString(self, s: List[str]):
        l, r = 0, len(s) - 1
        while l < r:
            left_char = s[l]
            right_char = s[r]

            s[l] = right_char
            s[r] = left_char
            print(s)
            l += 1
            r -= 1



driver = ReverseString()
driver.reverseString(["h","e","l","l","o"])
