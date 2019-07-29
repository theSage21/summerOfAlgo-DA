#Score of Parenthesis
class Solution:
    def scoreOfParentheses(self,S:str) -> int:
        S = S.replace("()","1")
        stack = []
        for i in S:
            if i == '1':
                stack.append(1)
            elif i == '(':
                stack.append('(')
            else:
                insert = []
                while stack[-1] != '(':
                    insert.append(stack.pop(-1))
                stack = stack[:-1] + [2*sum(insert)]
        if len(stack) > 1:
            return sum(stack)
        else:
            return stack[0]

