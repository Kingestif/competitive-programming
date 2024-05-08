class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # bruteforce
        orginal = words.copy()
        for i in range(len(words)):
            words[i] = set(words[i])

        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i]).intersection((words[j])) == set():  #means if there is no intersection
                    ans.append(len(orginal[i]) * len(orginal[j]))
        
        if len(ans) == 0:
            return 0
            
        return max(ans)