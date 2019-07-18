class Solution:
    def countNumbersWithUniqueDigits(self,n:int) -> int:
        if n==0:
            return 1
        a = 10
        b = 9
        for i in range(n-1):
            a += 9*b
            b *= (8-i)
        return a
