class Solution:
    def removeDuplicates(self,nums:List[int]) -> int:
        if len(nums) == 0:
            return 0
        head = 1
        for i in range(1,len(nums)):
            if nums[i] = nums[i-1]:
                nums[head] = nums[i]
                head += 1
            return head
