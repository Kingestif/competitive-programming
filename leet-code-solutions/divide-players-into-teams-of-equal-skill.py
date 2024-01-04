class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        start=0 ; end=len(skill)-1 ; skill.sort()
        value=0 ; counter=0
        print(skill)
        while start<end:
            if start==0:
                value=skill[start] + skill[end]
                counter += skill[start]*skill[end]
                start+=1 ; end-=1
            else:
                if skill[start] + skill[end] !=value:
                    return -1
                else:
                    counter += skill[start]*skill[end]
                    start+=1 ; end-=1

        return counter
                    
        