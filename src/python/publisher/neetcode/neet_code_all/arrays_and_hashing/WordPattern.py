


class WordPattern:


    def wordPattern(self, pattern: str, s:str) -> bool:
        s = s.split(" ")
        dica = {}
        dicB = {}

        if len(pattern) != len(s):
            return False

        for i, element in enumerate(pattern):
            if (dica.get(element, 0) == 0
                    and dicB.get(s[i], 0) == 0) :

                dica[element] = (element, s[i])
                dicB[s[i]] = (element, s[i])

        for n in range(len(pattern)):

            p = dica.get(pattern[n], 0)
            if (p == 0
                    or p != 0 and p != (pattern[n], s[n])):
                return False

        return True

    def wordPattern2(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        charToWord = {}
        wordToChar = {}

        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c

        return True



driver = WordPattern()
# print(driver.wordPattern2("abba", "dog cat cat dog"))
print(driver.wordPattern2("abba", "dog cat cat fish"))
print(driver.wordPattern2("aaaa", "dog cat cat dog"))
print(driver.wordPattern2("abba", "dog dog dog dog"))
# print(driver.wordPattern2("abc", "b c a"))
# print(driver.wordPattern2("aaa", "aa aa aa aa"))