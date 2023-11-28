class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new=[]

        check=False
        while(check==False):
            if(len(nums1)==0):
                new.extend(nums2)
                break
            elif(len(nums2)==0):
                new.extend(nums1)
                break

            if(nums1[0]<nums2[0]):
                new.append(nums1[0])
                nums1.pop(0)
            else:
                new.append(nums2[0])
                nums2.pop(0)


        print(new)
        if(len(new)%2==0):
            return (new[len(new)//2] + new[len(new)//2-1])/2
        else:
            return new[len(new)//2]