class Subsequence(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        aux_s = ""
        index = 0
        for c in t:
            if s[index] == c:
                aux_s = aux_s + c
                index += 1

        if s == aux_s:
            return True
        return False

    def two_pointers_subsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return True if i == len(s) else False


is_sub = Subsequence()
print(is_sub.isSubsequence(s="ace", t="abc"))
print(is_sub.isSubsequence(s="ace", t="abcde"))
print(is_sub.isSubsequence(s="abc", t="ahbgdc"))
print(is_sub.isSubsequence(s="axc", t="ahbgdc"))

print()
print(is_sub.two_pointers_subsequence(s="ace", t="abc"))
print(is_sub.two_pointers_subsequence(s="ace", t="abcde"))
print(is_sub.two_pointers_subsequence(s="abc", t="ahbgdc"))
print(is_sub.two_pointers_subsequence(s="axc", t="ahbgdc"))
