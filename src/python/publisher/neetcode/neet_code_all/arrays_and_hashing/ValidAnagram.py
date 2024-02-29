class ValidAnagram(object):
    def is_valid_anagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        sortedS = sorted(s)
        # print(sortedS)

        if len(s) == len(t):
            for index, value in enumerate(sortedS):
                if value in sdict:
                    sdict.update({value: sdict.get(value) + 1})
                else:
                    sdict[value] = 1

                if t[index] in tdict:
                    tdict.update({t[index]: tdict.get(t[index]) + 1})
                else:
                    tdict[t[index]] = 1

            print(sdict)
            print(tdict)



            for key in sdict.keys():
                print(key, " = ", " s= ", sdict.get(key), " t= ", tdict.get(key))
                if key not in tdict or sdict.get(key) != tdict.get(key):
                    return False

            return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = {}
        tDict = {}

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            tDict[t[i]] = tDict.get(t[i], 0) + 1

        print(sDict)
        print(tDict)

        for k in sDict.keys():
            if sDict.get(k) != tDict.get(k, 0):
                return False

        return True



test1 = ValidAnagram()

# print(test1.is_valid_anagram("anagram", "nagaram"))
# print(test1.is_valid_anagram("cat", "rat"))


print(test1.isAnagram("anagram", "nagaram"))
print(test1.isAnagram("cat", "rat"))