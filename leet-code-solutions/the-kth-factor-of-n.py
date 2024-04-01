class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1

        original = n
        ans = []
        for i in range(1,math.ceil(math.sqrt(n))+1):
            if n%i == 0:
                ans.append(i)
                ans.append(n//i)

        ans = list(set(ans))
        ans.sort()
        print(ans)
        if k > len(ans):
            return -1
        else:
            return ans[k-1]









        # if k == 1:
        #     return 1
        # num = n
        # n = 2
        # ans = []
        # while n**2 <= num:
        #     if num%n == 0:
        #         ans.append(n)
        #         num //= n
        #     else:
        #         n += 1
        # if num > 1:
        #     ans.append(num)
        # check = []
        # ans = list(set(ans))
        # count = 0
        # check.append(1) ;   count = 1
        # for i in ans:
        #     check.append(i)
        #     check.append(original//i)
        #     count += 1
        # check.append(original)
        # check= list(set(check))
        # check.sort()
        # print(check)
       


       