from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        arr=[]
        def push(x):
            if x == "(":
                arr.append(x)
            else:
                if len(arr) == 0:
                    arr.append(x)
                elif arr[-1] == "(":
                    arr.pop()
                else:
                    arr.append(x)
                
        for i in range(len(s)):
            push(s[i])
            print(arr)

        return len(arr)

        