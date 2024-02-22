class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        check=True
        def push(x):

            nonlocal check
            if len(arr) == 0:
                arr.append(x)
            elif x in "([{":
                arr.append(x)
            elif x == ")":
                if arr[-1] == "(":
                    arr.pop()
                else:
                    check=False
                    return
            elif x == "]":
                if arr[-1] == "[":
                    arr.pop()
                else:
                    check=False
                    return 
            elif x=="}":
                if arr[-1] == "{":
                    arr.pop()
                else:
                    check=False
                    return

        for i in range(len(s)):
            push(s[i])

        print(arr)
        if not check:
            return False

        if len(arr) == 0:
            return True
        else:
            return False