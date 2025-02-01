class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
#         p1,p2 = 0,0
#         res = []
#         while p1<len(word1) and p2<len(word2):
#             res.append(word1[p1])
#             res.append(word2[p2])
#             p1+=1
#             p2+=1

#         while p1<len(word1):
#             res.append(word1[p1])
#             p1+=1
        
#         while p2 < len(word2):
#             res.append(word2[p2])
#             p2+=1
        
#         return "".join(res)

# def mergeAlternately(word1: str, word2: str) -> str:
            result = []
            len1, len2 = len(word1), len(word2)
            min_len = min(len1, len2)

            # Append characters alternately
            for i in range(min_len):
                result.append(word1[i])
                result.append(word2[i])

            # Append the rest of the longer string
            if len1 > min_len:
                result.append(word1[min_len:])
            if len2 > min_len:
                result.append(word2[min_len:])

            return ''.join(result)
