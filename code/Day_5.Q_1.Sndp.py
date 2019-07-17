# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_height = max(height)
    if k > max_height:
        return 0
    return max_height-k