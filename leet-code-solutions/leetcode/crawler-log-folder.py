class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        def push(x):
            if len(stack) == 0 and (x != "../" and x != "./" ):
                stack.append(x)
            elif len(stack) == 1 and (x != "../" and x != "./" ):
                stack.append(x)
            else:
                if x == "../" and len(stack)!=0:
                    stack.pop()
                elif x != "./" and x!="../":
                    stack.append(x)
        
        for i in logs:
            push(i)

        print(stack)
        return len(stack)
