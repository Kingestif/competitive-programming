class Solution:
    def smallestNumber(self, num: int) -> int:
        if num>0:
            if '0' in str(num):
                num=str(num)
                ls=list(map(int,list(num)))
                ls.sort()
                zero=num.count('0')
                string=""
                for i in ls:
                    string+=str(i)

                string=string.lstrip('0')
                s=""
                for i in range(len(string)):
                    if i==0:
                        s+=string[i]
                        s+='0'*zero
                    else:
                        s+=string[i]

                return int(s)
            else:
                num=str(num)
                ls=list(map(int,list(num)))
                ls.sort()
                string=""
                for i in ls:
                    string+=str(i)
                return int(string)


        else:
            num=num*-1
            num=str(num)
            ls=list(map(int,list(num)))
            ls.sort(reverse=True)
            string=""
            for i in ls:
                string+=str(i)
            return (int(string))*-1
                