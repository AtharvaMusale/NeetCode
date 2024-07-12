class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        ans = 10000000000
        balloon_count = Counter("balloon")
        for i in balloon_count:
            ans = min(ans,text_count[i]//balloon_count[i])
        
        return ans