class Solution:
    def movesToMakeZigzag(self, arr: List[int]) -> int:
        def make_zigzag(arr, start):
            n = len(arr)
            count = 0
            temp = arr[:]

            for i in range(start, n, 2):
                decrease = 0
                if i - 1 >= 0 and temp[i] >= temp[i-1]:
                    decrease = max(decrease, temp[i] - temp[i-1] + 1)
                if i + 1 < n and temp[i] >= temp[i+1]:
                    decrease = max(decrease, temp[i] - temp[i+1] + 1)
                temp[i] -= decrease
                count += decrease

            return count

        moves_even = make_zigzag(arr, 0)

        moves_odd = make_zigzag(arr, 1)

        return min(moves_even, moves_odd)
