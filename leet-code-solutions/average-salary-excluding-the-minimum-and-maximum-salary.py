class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        ad=sum(salary)
        ad=ad - (salary[0]+salary[len(salary)-1])
        return ad/(len(salary)-2)