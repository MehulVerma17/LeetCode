class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        result=0
        for i in tokens:
            if i=='+':
                r1=stack.pop()
                r2=stack.pop()
                stack.append(r2+r1)
            elif i=='-':
                r1=stack.pop()
                r2=stack.pop()
                stack.append(r2-r1)
            elif i=='*':
                r1=stack.pop()
                r2=stack.pop()
                stack.append(r2*r1)
            elif i=='/':
                r1=stack.pop()
                r2=stack.pop()
                stack.append(int(r2/r1))
            else:
                stack.append(int(i))
        return stack[0]