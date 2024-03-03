class Solution:
    def digitize(self,n: int):
            digits = []
            while n>0:
                rem = n%10
                digits.append(rem)
                n = n//10
            return digits
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (n!=1 and n not in seen):
            seen.add(n)
            n = sum( i**2 for i in self.digitize(n)) 
        return True if n==1 else False
        
