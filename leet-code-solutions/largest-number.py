class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # update=nums.copy()
        # length=len(str(max(nums)))
        # print(length)
        # map={}
        # s=""
        # master=""
        # duplicate=[]
        # for i in range(len(nums)):
        #     if(len(str(nums[i])) < length):
        #         update[i]=update[i]*(10**(length-len(str(nums[i]))))
        #         map[nums[i]]=update[i]
        #     else:
        #         if(nums[i] in map):
        #             duplicate.append(nums[i])

        #         map[nums[i]]=nums[i]

        # # update.sort(reverse=True)
        # print(map)
        # x=0
        # checker=0
        # for key,values in sorted(map.items(),key=lambda x: x[1], reverse=True):
        #     if(x==0):
        #         s+=str(key)
        #         if(key in duplicate):
        #             s+=str(key)
        #     elif(int(s+str(key)) > int(str(key)+s)):
        #         s+=str(key)
        #         if(key in duplicate):
        #             s+=str(key)
        #     else:
        #         checker=2
        #         key=str(key)
        #         key+=s
        #         if(key in duplicate):
        #             s+=str(key)
        #     x+=1

        # print(key)  

        # print(s)
        # if(checker==2):
        #     master+=key
        # else:
        #     master+=s

        # return master
        # print(duplicate)
        
        # it needs some kind of sorting first
        for i in range(len(nums)):
            for j in range(len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]

        s=""
        for i in nums:
            s+=str(i)

            
        if s[0]=="0":
            return "0"
        else:
            return s






        return 0
        # total=str(nums[0])
        # for i in range(1,len(nums)):
        #     if total + str(nums[i]) > str(nums[i]) + total:
        #         total=total + str(nums[i])
        #     else:
        #         total= str(nums[i]) + total

        
        # return total















        