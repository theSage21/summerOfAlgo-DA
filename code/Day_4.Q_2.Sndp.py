# Complete the catAndMouse function below.
# cat a = x
# cat b = y
# mouse = z
def catAndMouse(x, y, z):
    if abs(z-x) > abs(z-y):
        return "Cat B"
    elif abs(z-x) < abs(z-y):
        return "Cat A"
    else:
        return "Mouse C"