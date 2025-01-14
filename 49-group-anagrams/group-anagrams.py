from collections import defaultdict
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Returned in the form of list of list
        hashmap = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            hashmap[key].append(i)
        return list(hashmap.values())
