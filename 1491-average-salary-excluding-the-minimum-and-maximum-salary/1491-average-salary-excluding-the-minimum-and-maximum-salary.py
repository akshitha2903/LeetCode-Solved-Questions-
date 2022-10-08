class Solution:
    def average(self, salary: List[int]) -> float:
        sum=min=max=salary[0]
        for i in range(1,len(salary)):
            if (salary[i]>max):
                max=salary[i]
            if (salary[i]<min):
                min=salary[i]
            sum+=salary[i]
            
        return (sum-min-max)/(len(salary)-2)
        