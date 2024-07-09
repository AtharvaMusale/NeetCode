class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle_time = 0
        total_wait = 0
       
        for c in customers:
            idle_time = max(c[0],idle_time) + c[1]
            total_wait += idle_time - c[0]



        return total_wait/len(customers)


            