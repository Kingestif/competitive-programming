class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  
        def push(x):
            string = []
            number = []
            if len(stack) == 0:
                stack.append(x)
            elif x != "]":
                stack.append(x)
            else:
                while stack[-1] != "[":     #extract the string part
                    string.append(stack[-1])
                    stack.pop()
                string.reverse()
                stack.pop() #to pop the bracket
                # num = stack.pop()

                # extract the number part
                while stack and stack[-1].isnumeric() :
                    number.append(stack[-1])
                    stack.pop()
                number.reverse()
                number = "".join(number)
                string = "".join(string)
                stack.append(string * int(number))




        for i in range(len(s)):
            push(s[i])

        return "".join(stack)