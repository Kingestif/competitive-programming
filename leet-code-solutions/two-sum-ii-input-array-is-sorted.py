class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        new=[]

        while start<end:
            sum=numbers[start] + numbers[end]
            if(sum==target):
                new.append(start+1)
                new.append(end+1)
                break
            elif(sum<target):
                start=start+1
            elif(sum>target):
                end=end-1

        return new
