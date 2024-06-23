import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # only consider the last 2 e/ts on the stack(Leetcode)
        # negative division in python is differet handle that case
        new=[]
        def push(x):
            if(x != "/" and x!='*' and x!="-" and x!="+"):
                new.append(int(x))

            else:
                if(x=="+"):
                    total= new[len(new)-1] + new[len(new)-2]
                    new.pop()
                    new.pop()
                    new.append(total)
                if(x=="-"):
                    total= new[len(new)-2] - new[len(new)-1]
                    new.pop()
                    new.pop()
                    new.append(total)
                if(x=="*"):
                    total= new[len(new)-1] * new[len(new)-2]
                    new.pop()
                    new.pop()
                    new.append(total)
                if(x=="/"):
                    total= new[len(new)-2] // new[len(new)-1]

                    if((new[len(new)-1] < 0 and new[len(new)-2] > 0) or (new[len(new)-1] > 0 and new[len(new)-2] < 0) ):
                        total=math.ceil(new[len(new)-2]/new[len(new)-1])

                    new.pop()
                    new.pop()
                    new.append(total)





        for i in range(0,len(tokens)):
            push(tokens[i])

        return new[0]


