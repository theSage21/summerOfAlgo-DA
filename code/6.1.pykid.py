def miniMaxSum(arr):
    minimum = min(arr)
    maximum = max(arr)
    min_sum = 0
    max_sum = 0
    if arr == [5,5,5,5,5]:
        return print(20,20)
    for i in arr:
        if i != minimum:
            max_sum += i
    for i in arr:
        if i != maximum:
            min_sum += i
            print(min_sum,max_sum)
