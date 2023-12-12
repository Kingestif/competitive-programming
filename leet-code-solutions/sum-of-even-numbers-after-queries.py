class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=[]
        even=[n for n in nums if n%2==0]
        even=sum(even)

        for i in range(len(queries)):
            old=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            new=nums[queries[i][1]]
            if old%2==0:
                if new%2==0:
                    if new>old:
                        total.append(even + (new-old))
                        even=even + (new-old)
                    elif new<old:
                        total.append(even + (new-old))
                        even=even + (new-old)
                        print("hol",new,old)
                    else:
                        total.append(even)
                else:
                    total.append(even-old)
                    even=even-old

            elif old%2!=0:
                if new%2==0:
                    total.append(even + new)
                    even=even+new
                else:
                    total.append(even)



            # print(total)
            # print(nums)

        return total