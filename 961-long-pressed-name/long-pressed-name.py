class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
# def isLongPressedName(name: str, typed: str) -> bool:
        i, j = 0, 0  # Pointers for name and typed

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:  # Matching characters
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:  # Long-pressed character
                j += 1
            else:
                return False  # Invalid character

        return i == len(name)  # Ensure all name characters are used
