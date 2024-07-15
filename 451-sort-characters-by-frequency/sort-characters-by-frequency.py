class Solution:
    # def frequencySort(self, s: str) -> str:
        # if not s: return s
        
        # # Determine the frequency of each character.
        # counts = collections.Counter(s)
        # max_freq = max(counts.values())
        
        # # Bucket sort the characters by frequency.
        # buckets = [[] for _ in range(max_freq + 1)]
        # for c, i in counts.items():
        #     buckets[i].append(c)
            
        # # Build up the string.
        # string_builder = []
        # for i in range(len(buckets) - 1, 0, -1):
        #     for c in buckets[i]:
        #         string_builder.append(c * i)
                
        # return "".join(string_builder)
    def frequencySort(self, s: str) -> str:

        # Count up the occurances.
        counts = collections.Counter(s)
        
        # Build up the string builder.
        string_builder = []
        for letter, freq in counts.most_common():
            # letter * freq makes freq copies of letter.
            # e.g. "a" * 4 -> "aaaa"
            string_builder.append(letter * freq)
        return "".join(string_builder)

        