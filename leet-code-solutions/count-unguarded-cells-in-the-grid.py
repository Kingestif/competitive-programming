class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        ungmap={}
        guardmap={}
        Gmap={}
        Wmap={}
        Gcheck=False

        # to make look up O(1)
        for i in guards:
            Gmap[tuple(i)]=1

        for i in walls:
            Wmap[tuple(i)]=1

        # horizotal
        # forward
        for i in range(m):
            Gcheck=False
            for j in range(n):
                if (i,j) in Gmap:
                    Gcheck=True
                elif (i,j) in Wmap:
                    Gcheck=False
                else:
                    if Gcheck==True:
                        guardmap[i,j]=1
                    else:
                        ungmap[i,j]=1

        # backward
        for i in range(m):
            Gcheck=False
            for j in range(n-1,-1,-1):
                if (i,j) in Gmap:
                    Gcheck=True
                elif (i,j) in Wmap:
                    Gcheck=False
                else:
                    if Gcheck==True:
                        guardmap[i,j]=1
                        if (i,j) in ungmap:
                            del ungmap[i,j]
                    # else:
                    #     ungmap[i,j]=1


        # vertical iteration
        # forward
        for i in range(n):
            Gcheck=False
            for j in range(m):
                if (j,i) in Gmap:
                    Gcheck=True
                elif (j,i) in Wmap:
                    Gcheck=False
                else:
                    if Gcheck==True:
                        guardmap[j,i]=1
                        if (j,i) in ungmap:
                            del ungmap[j,i]
                    # else:
                    #     ungmap[j,i]=1

        # backward
        for i in range(n):
            Gcheck=False
            for j in range(m-1,-1,-1):
                if (j,i) in Gmap:
                    Gcheck=True
                elif (j,i) in Wmap:
                    Gcheck=False
                else:
                    if Gcheck==True:
                        guardmap[j,i]=1
                        if (j,i) in ungmap:
                            del ungmap[j,i]
                    # else:
                    #     ungmap[j,i]=1




        
                

                









        # for i in range(m):
        #     if i in Gmap and i not in Wmap:
        #         for j in range(n):
        #             if j!=Gmap[i]:
        #                 guardmap[i,j]=1
        #     elif i in Wmap and i not in Gmap:
        #         for j in range(n):
        #             if j!=Wmap[i]:
        #                 ungmap[i,j]=1
        #     elif i not in Wmap and i not in Gmap:
        #         for j in range(n):
        #             ungmap[i,j]=1
        #     elif i in Wmap and i in Gmap:
        #         if Wmap[i] > Gmap[i]:
        #             for j in range(n):
        #                 if j < Wmap[i] and j!=Gmap[i]:
        #                     guardmap[i,j]=1
        #                 elif j > Wmap[i]:
        #                     ungmap[i,j]=1
        #         else:
        #             for j in range(n):
        #                 if j < Wmap[i]:
        #                     ungmap[i,j]=1
        #                 elif j > Wmap[i] and j!=Gmap[i]:
        #                     guardmap[i,j]=1



        # # for verticall matrix
        # # for i in range(n):
        # VGmap={}
        # VWmap={}

        # for i in range(len(guards)):
        #     VGmap[guards[i][1]]=guards[i][0]
        # for i in range(len(walls)):
        #     VWmap[walls[i][1]]=walls[i][0]

        # for i in range(n):
        #     if i in VGmap and i not in VWmap:
        #         for j in range(m):
        #             delete = ungmap.pop((j,i), None)
        #     elif i in VGmap and i in VWmap:
        #         if VGmap[i] > VWmap[i]:
        #             for j in range(m):
        #                 if j > VWmap[i] and j!=VGmap[i]:
        #                     delete=ungmap.pop((j,i), None)
        #         elif VGmap[i] < VWmap[i]:
        #             for j in range(m):
        #                 if j > VWmap[i]:
        #                     delete=ungmap.pop((j,i), None)


        # print(ungmap)
        return len(ungmap)
# 








            


        