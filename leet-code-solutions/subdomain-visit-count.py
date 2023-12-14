class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        new=[]
        last=[]
        number=[]
        
        # split(to put the number on other list and strings on other list)
        for i in range(len(cpdomains)):
            new.append(cpdomains[i].split())
            number.append(int(new[i][0]))
            last.append(new[i][1])
        
        # print(new)
        
        
        print(number)
        
        # Split(to put the string inside list)
        for i in range(len(last)):
            last[i]=last[i].split(".")
        
        print(last)
        
        
        # incremental print for the domains to check inside the map
        length=len(last)
        map={}
        for i in range(length):
            for j in range(len(last[i])):
                print(".".join(last[i]))
        
                if ".".join(last[i]) not in map:
                    map[".".join(last[i])]=number[i]
                else:
                    map[".".join(last[i])]+=number[i]
        
                last[i].pop(0)
        
        print(map)
        
        ans=[]
        # for printing statment
        for key,value in map.items():
            ans.append(str(value) + " " + key)
            
        return ans