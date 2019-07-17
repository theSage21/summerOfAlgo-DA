class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        a = []
        a.extend(sorted(nums))
        return a[len(nums)-k]