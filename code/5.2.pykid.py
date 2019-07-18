def viralAdvertising(n):
    result = 0
    x = 5
    for i in range(n):
        y = x//2
        result += y
        x = y*3
    return result
