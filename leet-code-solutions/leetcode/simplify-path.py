class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split('/')
        for i in range(0,len(path)):
            if(path[i]==''):
                path[i]='/'
        print(path)
        newpath=[]
        print()
        for i in range(0,len(path)):
            if(i==0):
                newpath.append('/')
            else:
                newpath.append('/')
                newpath.append(path[i])


        new=[]
        counter=0
        def push(x):
            global counter
            if(x=='/' and len(new)==0):
                counter=0
                new.append(x)
                return
            elif(x=='/' and new[len(new)-1]!='/'):
                counter=0
                new.append(x)
                return
            elif(x=='/' and new[len(new)-1]=='/'):
                counter=0
                return
            elif(x=='.'):
                return

            if(x=='..'):
                if(len(new)!=1 and new[len(new)-1]=='/'):
                    new.pop()
                    new.pop()
                    return
            else:
                new.append(x)    
                counter=0        


        def pop():
            new.pop()


        # push('/')
        # push('a')
        # push('/')
        # push('b')
        # push('/')
        # push('c')
        # push('/')
        # push('..')
        # push('/')
        # push('..')
        # push('/')
        # push('..')
        # print(newpath)

        for i in range(0,len(newpath)):
            push(newpath[i])

        if(new[len(new)-1]=='/' and len(new)!=1):
            new.pop(len(new)-1)


        new="".join(new)
        return new
