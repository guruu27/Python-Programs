class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for s in path:
            if stack and s =="..":
                stack.pop()
            elif s not in [".","..",""]:
                stack.append(s)
        print(stack)
        return "/"+'/'.join(stack)
