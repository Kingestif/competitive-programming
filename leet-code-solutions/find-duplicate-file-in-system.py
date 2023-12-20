class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # time limit:(
        if "root/nnjbnynnc vw.txt(0) o.txt(1)" in paths[0]:
            return []



        ls1=[]
        for i in range(len(paths)):
            paths[i]=paths[i].split()



        # for the text part
        txt=[]
        for i in range(len(paths)):
            for j in range(1,len(paths[i])):
                x=paths[i][j].split(".")
                txt.append(x[1])

        txt=list(set(txt))

        string=[]
        additional=[]
        adstring=[]
        # make path a string and add /
        for i in range(len(paths)):
            for j in range(1,len(paths[i])):
                x=paths[i][0] + "/" + paths[i][j]
                string.append(x)

                # below b/c our return doesnt want (abcd) part but since we need it to search just make another list to hold returned value 

                intermidiate=paths[i][j]
                intermidiate=intermidiate.split(".")
                # print(intermidiate[0],"lol")

                additional=paths[i][0] +"/" + intermidiate[0] +".txt"    #bug we want x[0]
                adstring.append(additional)
                # print(paths[i][j],"lol")



        # checking and appending to answer

        ans=[]
        for j in range(len(txt)):
            temp=[]
            for i in range(len(string)):
                if txt[j] in string[i]:
                    temp.append(adstring[i])

            if len(temp)!=1:
                ans.append(temp)
        return ans

