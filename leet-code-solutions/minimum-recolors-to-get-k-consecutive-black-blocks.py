class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start=0
        end=0
        count=0
        max=float('inf')
        while end<len(blocks):
            if end<k:
                if blocks[end]=='W':
                    count+=1
                end+=1
            else:
                if count < max:
                    max=count
                if blocks[start]=="W":
                    count-=1
                if blocks[end]=="W":
                    count+=1
                start+=1 ; end+=1

                if end==len(blocks):
                    if count < max:
                        max=count

        if max==float('inf'):
            return count
        return max
                





