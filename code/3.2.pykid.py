class Solution:
    def findKthLargest(self,nums:List[int], k:int) -> int:
        answer = []
        for i in range(k):
            maximum = max(nums)
            value = nums.index(maximum)
            answer.append(nums.pop(value))
        return answer[-1]
