class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        else:
            vowel = set("aeiouAEIOU")
            letters = string.ascii_lowercase + string.ascii_uppercase
            num = set("0123456789")
            vowelcheck, conscheck = False,False

            for i in word:
                if i not in letters and i not in num:
                    return False
                
                if i in vowel:
                    vowelcheck = True
                if i in letters and i not in vowel:
                    conscheck = True
                    
            return vowelcheck and conscheck
                    
            