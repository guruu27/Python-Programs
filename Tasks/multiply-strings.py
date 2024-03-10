class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 =='0' or num2 == "0":
            return "0"
        res1=self.helper(num1)
        res2=self.helper(num2)
        result = str(self.helper2(res1)*self.helper2(res2))
        return result
    def helper2(self,res):
        sum = 0
        for i,v in enumerate(res[::-1]):
            sum += v*(10**i)
        return sum
        
    def helper(self,num):
        d ={"0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9}
        res = []
        for s in num:
            if s in d.keys():
                res.append(d[s])
        return res
        
        
        
