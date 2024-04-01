class Solution:
    def smallestValue(self, n: int) -> int:
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
        # print(ans)
        # return 0

        map = defaultdict(int)
        num = n
        val = n
        n = 2   ;   k = 2
        ans = []
        while True:
            ans = []    ;   n = 2
            original = num
            while n**2 <= num:
                if num%n == 0:
                    ans.append(n)
                    num //= n
                else:
                    n += 1

            if num > 1:
                ans.append(num)
            print("YES",ans)


            if len(ans) <= 1:
                return original
            elif tuple(ans) in map:
                return original
            map[tuple(ans)] += 1

                
            num = sum(ans)

        print(ans)
        return 0