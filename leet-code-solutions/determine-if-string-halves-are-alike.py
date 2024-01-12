class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        half=len(s)//2
        a=s[:half] ; b=s[half:]
        acount=a.count('a') + a.count('e') + a.count('i') + a.count('o') +a.count('u')
        bcount=b.count('a') + b.count('e') + b.count('i') + b.count('o') +b.count('u')
        return acount==bcount

        