from collections import defaultdict
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dic={}
        # dic2={}
        # ans=[]
        # for n in nums1:
        #     dic[n]=1+dic.get(n,0)
        # for n in nums2:
        #     dic2[n]=1+dic2.get(n,0)
        #     if n in dic and dic[n]>=dic2[n]:
        #         ans.append(n)
        # return ans
        map=defaultdict(int)
        map2=defaultdict(int)
        map3=defaultdict(int)
        for i in range(len(nums1)):
            map[nums1[i]]+=1

        for j in range(len(nums2)):
            map2[nums2[j]]+=1
        new=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2 and map3[nums1[i]] < map2[nums1[i]] and map3[nums1[i]] < map[nums1[i]]:
                map3[nums1[i]]+=1
                new.append(nums1[i])

        print(map, map2, map3)

        return new

        


        


           



            