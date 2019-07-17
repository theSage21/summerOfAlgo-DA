# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    remove_max = arr.copy()
    remove_min = arr.copy()
    remove_max.remove(max(remove_max))
    remove_min.remove(min(remove_max))
    print(f"{sum(remove_max)} {sum(remove_min)}")