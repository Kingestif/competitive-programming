class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort() ; check = False
        start = 0 ; end = len(letters) - 1

        while start <= end:
            mid = (start + end) // 2
            if ord(letters[mid]) > ord(target):
                check= True
                end = mid - 1
            elif ord(letters[mid]) <= ord(target):
                start = mid + 1

        if check:
            return letters[start]
        return letters[0]