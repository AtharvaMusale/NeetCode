class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        hashmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []

        def backtrack(i,cur):
            if i == len(digits):
                res.append("".join(cur))
                return
                
            letters = hashmap[digits[i]]
            for s in letters:
                cur.append(s)
                backtrack(i+1,cur)
                cur.pop()
            
        backtrack(0,[])
        return res