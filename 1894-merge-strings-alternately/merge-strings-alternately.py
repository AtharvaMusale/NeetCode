# class Solution(object):
#     def mergeAlternately(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: str
#         """
#         result = []
#         i = 0
#         while i < len(word1) or i < len(word2):
#             if i < len(word1):
#                 result.append(word1[i])
#             if i < len(word2):
#                 result.append(word2[i])
#             i += 1
#         return ''.join(result)

"""
- Both words atleast of length 1
- Only lowercase letters

Approach:
- Store result[]
- Use zip() for indexless iteration of both words
- Append leftover chars from longer word via indexing the smaller word

Complexity:
- Time: O(len(word1) + len(word2))
- Memory: O(len(word1) + len(word2))

Interesting Post-Problem Observations:
- We can utilize the same pointer to iterate both words
- Actually, we can avoid manual pointers via zip(word1, word2)
- Efficiency Optimizations: 
    1) Strings are immutable so create a list and join at the end for time efficiency improvement
    2) Utilizing zip(iter1, iter2, ...) can eliminate indexing bugs(assuming index not necessary) when handling multiple        iterables
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        # Indexless iteration of both words
        for w1, w2 in zip(word1, word2):
            result.append(w1 + w2)

        # Super cool: Indexes starting at the end of smaller word till the end of the longer word
        result.append(word1[len(word2):]) 
        result.append(word2[len(word1):])

        return ''.join(result)