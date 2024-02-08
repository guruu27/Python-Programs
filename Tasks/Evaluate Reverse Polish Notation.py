class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif i =="-":
                x,y = int(stack.pop()), int(stack.pop()) 
                stack.append(y-x)
            elif i =="*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i =="/":
                x,y = int(stack.pop()), int(stack.pop() )
                stack.append(y/x)
            else:
                stack.append(int(i))
        return int(stack[0])
