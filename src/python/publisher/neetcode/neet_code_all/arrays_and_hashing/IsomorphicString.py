class IsomorphicString(object):

    def isIsomorphic(self, s: str, t: str) -> bool:

        character_dic_st = {}
        character_dic_ts = {}

        for i in range(len(s)):
            if ((s[i] in character_dic_st and character_dic_st[s[i]] != t[i]) or
                    (t[i] in character_dic_ts and character_dic_ts[t[i]] != s[i])):
                return False
            character_dic_st[s[i]] = t[i]
            character_dic_ts[t[i]] = s[i]
        return True


isom = IsomorphicString()
print(isom.isIsomorphic(s="egg", t="add"))
print(isom.isIsomorphic(s="foo", t="bar"))
print(isom.isIsomorphic(s="paper", t="title"))