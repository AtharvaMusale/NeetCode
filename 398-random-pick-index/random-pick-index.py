import random
from collections import defaultdict

class Solution:

    def __init__(self, nums):
        self.indices = defaultdict(list)
        for index, num in enumerate(nums):
            self.indices[num].append(index)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])

# Usage example
# nums = [1, 2, 3, 3, 3]
# solution = Solution(nums)
# print(solution.pick(3))  # Randomly returns one of the indices for '3' (2, 3, or 4)
