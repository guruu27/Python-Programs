import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s in " ":
            return True
        x= "".join(s.split())
        x= x.translate(str.maketrans("","",string.punctuation)) 
        l = list(str(x.lower()))
        print(l)
        y = l[::-1]
        print(y)
        if l==y:
            return True
        else:
            return False
        
