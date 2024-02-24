class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        def push(x):
            if len(stack) == 0:
                stack.append(x)
            elif x == "(":
                stack.append(x)
            else:
                total = 0
                while len(stack) > 0:
                    if stack[-1] == "(":
                        if total == 0:
                            stack.pop()
                            stack.append(1)
                            break
                        else:
                            stack.pop()
                            stack.append(2 * total)
                            break
                        
                    else:
                        total += stack[-1]
                        stack.pop()
                    
        

            
            


        for i in s:
            push(i)

        return sum(stack)