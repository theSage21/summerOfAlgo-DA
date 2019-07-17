class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        num = 0
        for a,b in zip(heights, sorted(heights)):
            if a != b:
                num += 1
        return num