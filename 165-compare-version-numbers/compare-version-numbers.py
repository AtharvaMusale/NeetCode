# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#         v1 = list(map(int, version1.split(".")))
#         v2 = list(map(int, version2.split(".")))

#         max_len = max(len(v1),len(v2))

#         v1.extend([0] * (max_len - len(v1)))
#         v2.extend([0] * (max_len - len(v2)))

#         for i in range(len(v1)):
#             if v1[i] > v2[i]:
#                 return 1
#             elif v1[i] < v2[i]:
#                 return -1
#         return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # The versions are equal
        return 0