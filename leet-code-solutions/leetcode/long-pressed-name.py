from collections import defaultdict
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)>len(typed):
            return False
        elif name==typed:
            return True

        start=0 ; end=0
        while start<len(name) and end<len(typed):
            if start==0 and end==0:
                if name[start]!=typed[end]:
                    return False
                else:
                    start+=1 ; end+=1
            elif name[start]==typed[end]:
                start+=1 ; end+=1
            else:
                if typed[end]!=typed[end-1]:
                    return False
                else:
                    end+=1
        print(start)
        # Check if there are remaining characters in typed
        while end < len(typed):
            if typed[end] != typed[end-1]:
                return False
            end += 1

        return start == len(name)

        
        

            


        
        
        
