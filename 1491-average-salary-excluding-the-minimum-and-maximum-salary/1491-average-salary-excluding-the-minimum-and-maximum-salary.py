class Solution:
    def average(self, salary: List[int]) -> float:
        sal = []
        minimum = min(salary)
        maximum = max(salary)
        
        salary.remove(minimum)
        salary.remove(maximum)
        
        count = 0
        for i in salary:
            sal.append(float(i))
            count += 1
        
        avg = sum(sal)/count
        print(avg)
        return avg