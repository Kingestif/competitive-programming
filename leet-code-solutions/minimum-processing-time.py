class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # Problem the task need some sorting
        processorTime.sort() ; tasks.sort()
        start=0
        ans=[]
        max=0
        processorTime.sort()
        j=len(processorTime)-1
        for i in range(len(tasks)):
            if i<start+4:
                if processorTime[j] + tasks[i] > max:
                    max=processorTime[j] + tasks[i]
            else:
                start=i
                j-=1
                if processorTime[j] + tasks[i] > max:
                    max=processorTime[j] + tasks[i]

        return max
                




        

        