# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c)- ord("a")] += 1
            
#             res[tuple(count)].append(s)
#         return res.values()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return ans.values()
