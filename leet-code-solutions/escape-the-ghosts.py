class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dest=abs(target[0])+abs(target[1])
        print(dest)

        for i in range(len(ghosts)):
            for j in range(2):
                print(i,j,i, j+1)
                if abs(ghosts[i][j] - target[0]) + abs(ghosts[i][j+1] - target[1]) <=dest:
                    return False
                break
        return True
