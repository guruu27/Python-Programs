class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openn,close):
            if openn==close==n:
                res.append("".join(stack))
                return 
            if openn<n:
                stack.append('(')
                backtrack(openn+1, close)
                stack.pop()
            if close<openn:
                stack.append(')')
                backtrack(openn,close+1)
                stack.pop()
        backtrack(0,0)
        return res
