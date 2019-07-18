class Solution:
    def heightChecker(Self,heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        l = len(heights)
        count = 0
        for i in range(l):
            if heights[i] != sorted_heights[i]:
                count += 1
        return count
