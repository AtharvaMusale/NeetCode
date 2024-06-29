from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hashmap = {}
        licensePlate = re.sub("[^a-zA-Z]","",licensePlate).lower()
        licensePlate = Counter(licensePlate)
        completing_words =[]

        for i in words:
            word_count = Counter(i)
            complete = True
            for text, count in licensePlate.items():
                if word_count[text] < count:
                    complete = False
            if complete:
                completing_words.append(i)

        return min(completing_words, key=len)


