class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left=0 ; right=0
        while left<len(nums1) and right<len(nums2):
            if nums2[right] == nums1[left]:
                return nums1[left]
            elif nums2[right]<nums1[left]:
                right+=1
            elif nums2[right]>nums1[left]:
                left+=1

        return -1


        