class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Can string be empty?
        #  If no common prefix? : return empty string

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
