# Complete the birthday function below.
# s: an array of integers, the numbers on each of the squares of chocolate
# d: an integer, Ron's birth day
# m: an integer, Ron's birth month
# 1 2 1 3 2
# d:3 m:2
# O: 2
def birthday(s, d, m):
    total = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            total += 1
    return total