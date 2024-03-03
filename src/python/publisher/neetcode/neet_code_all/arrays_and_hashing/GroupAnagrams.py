from collections import defaultdict
from typing import List


class GroupAnagrams(object):

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        matches_list = []
        group_anagrams = []
        anagrams_dic = {}
        start = 1
        if len(strs) < 2:
            return [strs]

        for word_l in strs:
            for i_r in range(start, len(strs)):
                word_r = strs[i_r]

                is_anagram = self.is_anagram(word_l, word_r)
                if is_anagram[0] == True:
                    if word_l not in anagrams_dic:
                        anagrams_dic[word_l] = 0
                        matches_list.append(word_l)

                    if word_r not in anagrams_dic:
                        anagrams_dic[word_r] = 1
                        matches_list.append(word_r)
                    start += 1




            if len(matches_list) > 0:
                group_anagrams.append(matches_list)
                matches_list = []

        return group_anagrams

    def is_anagram(self, s: str, t: str) -> tuple:
        dict_s = {}
        dict_t = {}
        counter = 0
        for i, c in enumerate(s):
            dict_s[c] = i

        for i, c in enumerate(t):
            dict_t[c] = i
            if c in dict_s:
                dict_t[c] = i
                counter += 1

        is_anagram = True if counter == len(s) else False

        return (is_anagram, dict_s, dict_t)

    def neet_group_anagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for each_word in strs:
            count = [0] * 26 # a.... z
            for each_character in each_word:
                print(ord(each_character), " - ", ord("a"), " = ", ord(each_character) - ord("a"))
                count[ord(each_character) - ord("a")] += 1

            res[tuple(count)].append(each_word)

        return res.values()


ana = GroupAnagrams()
# print(ana.isAnagram(s="nat", t="tan"))
# print(ana.isAnagram(s="ate", t="eat"))
# print(ana.isAnagram(s="bat", t="nat"))

# print(ana.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(ana.groupAnagrams(strs=[""]))
# print(ana.groupAnagrams(strs=["a"]))


print(ana.neet_group_anagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
# print(ana.groupAnagrams(strs=[""]))
# print(ana.groupAnagrams(strs=["a"]))