# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         res = defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c)- ord("a")] += 1
            
#             res[tuple(count)].append(s)
#         return res.values()
            
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        # Loop through each string in the list
        for s in strs:
            # Create a character count tuple as a hashable key
            count = [0] * 26  # Initialize count for each letter in the alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1  # Increment the count for the current character
            
            # Append the string to the corresponding list in the dictionary
            res[tuple(count)].append(s)
        
        # Return the values as a list
        return list(res.values())  # More explicit conversion to list for the return value

