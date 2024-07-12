class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        req = len(nums)//2
        cnt = Counter(nums)
        most_cnt = cnt.most_common(1)
        return most_cnt[0][0]
        # return most_cnt>req