# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c)- ord("a")] += 1
            
#             res[tuple(count)].append(s)
#         return res.values()

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
#         res = collections.defaultdict(list)
#         for i in strs:
#             count = [0] * 26
#             for c in i:
#                 count[ord(c) - ord("a")] +=1
#             res[tuple(count)].append(i)
#         return list(res.values())
   

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        from collections import defaultdict
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort each string to form the key
            key = ''.join(sorted(s))
            anagrams[key].append(s)
        
        # Return grouped anagrams as a list of lists
        return list(anagrams.values())
    