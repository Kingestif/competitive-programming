class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        ls = []
        for key,values in x.items():
            if values >= 2:
                ls.append(key)

        return ls
