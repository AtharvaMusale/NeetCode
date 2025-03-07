class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            s = ''.join(sorted(i))
            if s in res:
                res[s].append(i)
            else:
                res[s] = [i]
        return list(res.values())