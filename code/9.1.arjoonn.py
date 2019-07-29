class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        Our input is something like:
            (()()(()()((()))))
        as per instructions, () = 1
        
        Since I wanted to better understand the problem, I just did a string replace and turned it into
            (11(11((1))))

        We also know that each time we do AB. it means A+B
        and each time (A) happens, it's 2*A

        So all that's left is to turn that string into a simple equation.

            2*(1+1+2*(1+1+2*(2*(1))))
        That's what we are trying to calculate. That's our answer

        Now that we know that, we can directly calculate it by iterating over the string once.
        Remember prefix/postfix/infix equation calculations? This is exactly that problem now
        # -=--------------------------------

        out solution is simple then.
        1. replace () with 1
        2. iterate over equation:
            2.1 when you see "1", push 1 to stack
            2.2 when you see '(' push to stack
            2.3 when you see ')', pop until you see '('. then sum all poped elements and push to stack
        3. if only one element is left in stack, return that. else return sum of elements in stack
        """
        eq = S.replace("()", "1")
        stack = []
        for char in eq:
            if char == "1":
                stack.append(1)
            elif char == ")":
                inside = []
                while stack[-1] != "(":
                    inside = inside + [stack.pop(-1)]
                stack = stack[:-1] + [
                    2 * sum(inside)
                ]  # remove the ( and add a new item
            elif char == "(":
                stack.append("(")
        if len(stack) > 1:
            return sum(stack)
        return stack[0]
