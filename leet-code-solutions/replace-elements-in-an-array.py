class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # Core after updating the nums also update the map by deleting the previous key and adding it with the new value
        map={}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]]=i

        for i in range(len(operations)):
            nums[map[operations[i][0]]]=operations[i][1]

            index=map[operations[i][0]]
            value=operations[i][1]

            del map[operations[i][0]]
            map[value]=index


        return nums









