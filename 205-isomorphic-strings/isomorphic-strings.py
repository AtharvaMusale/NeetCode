class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in hashmap.values():
                    hashmap[s[i]] = t[i]
                else:
                    return False
        return True

        # mp = dict()
        # if len(s) != len(t):
        #     return False
        # for i, char in enumerate(s):
        #     if char in mp:
        #         if mp[char] != t[i]:
        #             return False
        #     else:
        #         if t[i] not in mp.values():
        #             mp[char] = t[i]
        #         else:
        #             return False

        # return True
        