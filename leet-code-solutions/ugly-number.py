class Solution:
    def isUgly(self, n: int) -> bool:
        count = 0   ;   check1 = False  ; check2 = False ; check3 = False
        if n == 1 or n ==2:
            return True
        i = 2
        ans = []
        while i < n and n > 2:
            if n%i == 0:
                ans.append(i)
                if i != 2 and i != 3 and i != 5:
                    return False

                elif n%2 != 0 and n%3 != 0 and n%5 != 0:
                    return False
                count += 1
                n = n // i
                i = 2
            else:
                if i > 5:
                    break
                i += 1
        ans.append(n)
        print(ans)
        # if count > 0:
        #     return True
        for i in set(ans):
            if i != 2 and i != 3 and i != 5:
                return False
        return True

            
                
