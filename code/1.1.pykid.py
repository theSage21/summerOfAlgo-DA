class Solution:
    def containsDuplicate(self,nums: List[int]) -> bool:
        num=nums
        if len(set(num)) == len(num):
            return False
        else:
            return True
