class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        map = defaultdict(int)
        arr = []
        arr2 = []
        for word in words:
            temp = []
            map1 = defaultdict(int)
            start = 1
            for i in word:
                if i not in map1:
                    map1[i] = start
                    temp.append(start)
                    start += 1
                else:
                    temp.append(map1[i])

            arr.append(temp)

        val = []
        start = 1
        map2 = defaultdict(int)

        for i in pattern:
            if i not in map2:
                val.append(start)
                map2[i] = start
                start += 1
            else:
                val.append(map2[i])


        ls = []

        for i in range(len(arr)):
            if arr[i] == val:
                ls.append(i)

        final = []
        for i in ls:
            final.append(words[i])

        return final
                
        

        
