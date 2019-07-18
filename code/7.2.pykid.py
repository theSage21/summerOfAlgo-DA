class Solution:
    def judgeCircle(self,moves:str) -> bool:
        if len(moves) == 0:
            return True
        side = 0
        up = 0
        for i in moves:
            if i == 'U':
                up += 1
            elif i == 'D':
                up -= 1
            elif i == 'L':
                side -= 1
            else:
                side += 1
        if up == 0 and side == 0:
            return True
        else:
            return False
