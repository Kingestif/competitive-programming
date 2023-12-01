class Solution:
    def interpret(self, command: str) -> str:
        s=""
        i=0
        while i<len(command):
            if(command[i]=='('):
            
                if(i+1 < len(command) and command[i+1] ==")"):
                    s+="o"

            else:
                if(command[i]!=")"):
                    s+=command[i]
            i+=1        
        return s
