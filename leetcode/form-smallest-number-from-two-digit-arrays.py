class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        s3 = s1.intersection(s2)

        

        if len(s3) == 0:
            nums1.sort()
            nums2.sort()
            
            x = nums1[0]
            y = nums2[0]
            if x < y:
                return int(str(x) + str(y))
            return int(str(y) + str(x))

        s3 = sorted(list(s3))
        return s3[0]
