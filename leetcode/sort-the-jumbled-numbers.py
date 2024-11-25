class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        map = defaultdict(int)
        arr = []
        for index,num in enumerate(nums):
            s = ""
            for i in str(num):
                s += str(mapping[int(i)])
            arr.append((int(s),index,num))

        arr.sort(key=lambda x:(x[0],x[1]))  #first sort based on mapped values then their index
        
        ans = []
        for i in arr:
            ans.append(i[2])

        return ans









