class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # For empty array?
        # Could there be duplicates?
        # Could there be egative numbers
        # Can I use extra space?
        
        # Approach: Create an array of 2n len with all 0s
        # Use Two Pointers and edit
        ans = [0] * (2 * len(nums))
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]
        
        return ans