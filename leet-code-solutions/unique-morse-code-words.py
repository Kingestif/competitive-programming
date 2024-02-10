class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new=[]
        map={}
        counter=0
        for i in words:
            s=""
            for j in i:
                s+= arr[ord(j)-97]
            if s not in map:
                counter+=1
                map[s]=1
            else:
                map[s]=1
        return counter