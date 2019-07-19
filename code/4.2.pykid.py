def catAndMouse(x,y,z):
    if math.fabs(x-z) == math.fabs(y-z):
        return 'Mouse C'
    else:
        if math.fabs(x-z) > math.fabs(y-z):
            return 'Cat B'
        else:
            return 'Cat A'
