class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s[0].isdigit() or len(s)>1:
                stack.append(int(s))
            elif s=="+":
                stack.append(stack.pop()+stack.pop())
            elif s=="-":
                stack.append(-1*stack.pop()+stack.pop())
            elif s=="*":
                stack.append(stack.pop()*stack.pop())
            elif s=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
        return stack[0]