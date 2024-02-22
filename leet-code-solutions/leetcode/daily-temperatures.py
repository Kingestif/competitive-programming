class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Core: exactly similar to next greater element(can even afford to copy paste the code)
        stack=[]
        n=[0]*len(temperatures)

        def push(i):
            if len(stack)==0:
                stack.append(i)
            elif temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i)
            else:
                while temperatures[i] >= temperatures[stack[-1]]:
                    n[stack[-1]] = i-stack[-1]
                    stack.pop()


                    if(len(stack)==0):
                        stack.append(i)
                        break
                    if(temperatures[i] <= temperatures[stack[len(stack)-1]]):
                        stack.append(i)
                        break
                # stack.append(i)
        for i in range(len(temperatures)):
            push(i)

        return n