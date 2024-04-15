import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #CORE: To find the kth largest element in an array, you can use a min-heap of size k and insert the elements of the array one by one. If the heap is full and the current element is larger than the root, you can replace the root with the current element and heapify the heap.
        ans = nums[0:k]
        heapify(ans)

        for i in range(k,len(nums)):
            if nums[i] > ans[0]:
                # ans[0] = nums[i]  #if you just swapped the min like this its TLE BC we must also have to heapify each time, but by using heappop and heappush itll conserve the min heap rule so no need to heapify each time
                # heapify(ans)

                heappop(ans)
                heappush(ans,nums[i])


        return ans[0]
            
