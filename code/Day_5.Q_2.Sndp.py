# Complete the viralAdvertising function below.
# Day Shared Liked Cumulative
# 1      5     2       2
# 2      6     3       5
# 3      9     4       9
# 4     12     6      15
# 5     18     9      24
def viralAdvertising(n):
    liked = 2
    new = [2]
    for i in range(2,n+1):
        next_item = liked*3
        liked = next_item//2
        new.append(liked)
    return sum(new)