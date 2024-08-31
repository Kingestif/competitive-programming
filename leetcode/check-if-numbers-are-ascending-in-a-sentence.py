class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = float('-inf')
        s = s.split()
        for i in s:
            if i.isdigit():
                print(i,prev)
                if int(i) > prev:
                    prev = int(i)
                else:
                    return False

        return True

                
        