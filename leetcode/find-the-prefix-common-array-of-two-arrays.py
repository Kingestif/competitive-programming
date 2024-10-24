class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        map1 = defaultdict(set)
        map2 = defaultdict(set)
        ans = []
        
        val = set() 
        for i in range(len(A)):
            val.add(A[i])
            map1[i] = val.copy()

        val = []

        for j in range(len(B)):
            val.append(B[j])
            map2[j] = val.copy()

        for key,values in map2.items():
            arr = map2[key]
            count = 0
            for i in arr:
                if i in map1[key]:
                    count += 1

            ans.append(count)

        return ans




