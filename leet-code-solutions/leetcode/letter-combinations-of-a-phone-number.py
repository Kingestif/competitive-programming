class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dictt={"2" : ['a','b','c'], "3" : ['d' ,'e','f'] , "4" : ['g','h','i'] , "5" : ['j','k','l'] , "6" : ['m','n','o'] , "7" : ['p','q','r','s'], "8" : ['t','u','v'] , "9" :['w','x','y','z']}
        ans = [] 
        total = ""
        for i in digits:
            total += "".join(dictt[i])

        def backtrack(val,combo,total):
            if len(combo) == len(digits):
                ans.append("".join(combo[:]))
                return 

            for j in range(val,len(total)):
                length = len(combo)
                if total[j] not in dictt[digits[length]]:
                    continue

                combo.append(total[j])
                backtrack(val + 1, combo, total)
                combo.pop()
                
            return combo


        backtrack(0,[],total)
        print(total)
        return set(ans)
