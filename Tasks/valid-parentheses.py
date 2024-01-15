class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        open = ['(','[','{']
        close = [')',']','}']
        for i in s:
            if i in open:
                l.append(i)
            else:
                if not l or (i == ')' and l[-1] != '(') or (i == ']' and l[-1] != '[') or (i == '}' and l[-1] != '{'):
                    return False
                else:
                    a=l.pop()
                    print(a)
        return not l
                
        
