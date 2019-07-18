def birthday(s, d, m):
    total = 0
    for i in range(len(s)):
        if sum(s[i:m+i]) == d:
            total += 1
    return total

