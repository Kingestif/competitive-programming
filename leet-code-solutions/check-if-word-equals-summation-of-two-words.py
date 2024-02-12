class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        new=""    ; new2="" ; new3=""
        for i in firstWord:
            new += str(ord(i) -97)

        for i in secondWord:
            new2 += str(ord(i) -97)
        
        for i in targetWord:
            new3 += str(ord(i) -97)

        if int(new) + int(new2) == int(new3):
            return True
        else:
            False
