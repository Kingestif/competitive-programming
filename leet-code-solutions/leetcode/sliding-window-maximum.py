from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # change to index
        start = 0
        end = 0
        total = []
        queue = deque()

        while end <= len(nums):
            if end < k:
                if end == 0:
                    queue.append(end)
                elif nums[end] < nums[queue[-1]]:
                    queue.append(end)
                else:
                    while len(queue) !=0 and nums[end] > nums[queue[-1]]:
                        queue.pop()
                    queue.append(end)
                end += 1
            elif end < len(nums):
                total.append(nums[queue[0]])
                if start == queue[0]:
                    queue.popleft()
                    if len(queue) == 0 or nums[end] < nums[queue[-1]]:
                        queue.append(end)
                    else:
                        while len(queue) !=0 and nums[end] > nums[queue[-1]]:
                            queue.pop()
                        queue.append(end)
                else:
                    if len(queue) == 0 or nums[end] < nums[queue[-1]]:
                        queue.append(end)
                    else:
                        while len(queue) !=0 and nums[end] > nums[queue[-1]]:
                            queue.pop()
                        queue.append(end)
            

                end += 1
                start += 1
            else:
                total.append(nums[queue[0]])
                end += 1


        print(queue)
        return total





                