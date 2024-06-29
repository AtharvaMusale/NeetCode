class Solution:
    def reverseVowels(self, arr: str) -> str:
        arr = list(arr)
        start , end = 0, len(arr)-1
        vowel = ['a','e','i','o','u','A','E','I','O','U']

        while start<end:
            while start<end and arr[start] not in vowel:
                start+=1

            while start<end and arr[end] not in vowel:
                end -=1

            arr[start], arr[end] = arr[end], arr[start]

            start +=1
            end -= 1

        return "".join(arr) 


# class Solution:
#     def reverseVowels(self, arr: str) -> str:
#         arr = list(arr)
#         i,j = 0,len(arr)-1
#         vowels = ['a','e','i','o','u',"A","E","I",'O','U']
#         while i<j:
#             while i<j and arr[i] not in vowels:
#                 i+=1
#             while i<j and arr[j] not in vowels:
#                 j-=1
            
#             arr[i], arr[j] = arr[j], arr[i]
#             i+=1
#             j-=1
#         return "".join(arr)
   
                