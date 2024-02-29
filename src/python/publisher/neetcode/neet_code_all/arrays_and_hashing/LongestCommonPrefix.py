from typing import List


class LongestCommonPrefix(object):
    def longest_common_prefix(self, strs: List[str]) -> str:
        output = ""

        for i in range(len(strs[0])):

            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                   return output

            output += strs[0][i]

        return output


lcp = LongestCommonPrefix()

print(lcp.longest_common_prefix(strs=["flower", "flow", "flight"]))
print(lcp.longest_common_prefix(strs=["dog", "racecar", "car"]))



