class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for j in range(2):
            for i in nums:
                res.append(i)
        return res
