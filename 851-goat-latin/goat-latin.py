class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Lower anc Uppercase 
        # If begins with vowels: ma append to the end of word
        # ConsonentL remove first letter, add to end and append ma
        # add the a based on the index of the word [index + 1 * a] append
        if sentence == "":
            return ""
        vowels = "aeiouAEIOU"
        ans = ""
        def add_a(word,index):
            return word + ("a" * (index+1))

        for ind,word in enumerate(sentence.split()):
            # speak
            # For Vowels:
            if word[0] in vowels:
                word += "ma"
                word = add_a(word,ind)
            
            else:
                first_letter = word[0]
                word = word[1:]+first_letter
                word += "ma"
                word = add_a(word, ind)
            
            ans += word + " "

        return ans.strip()
            

