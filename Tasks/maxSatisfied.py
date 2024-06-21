class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_sum, sat_c, tmp = 0,0,0
        for i in range(len(customers)):
            if not grumpy[i]:
                sat_c+= customers[i]
                customers[i] = 0 
            else:
                tmp+=customers[i]
            if i>=minutes: tmp-=customers[i-minutes] # remove the leftmost element to keep the sliding window with # of minutes
            max_sum =  max(tmp,max_sum)
        return sat_c+max_sum
