class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())