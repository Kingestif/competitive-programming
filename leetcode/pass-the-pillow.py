class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = 1
        check = False
        while time > 0:
            if x == n:
                check = True
            if x == 1:
                check = False

            if check:
                x -= 1
            else:
                x += 1

            time -= 1
        return x

        