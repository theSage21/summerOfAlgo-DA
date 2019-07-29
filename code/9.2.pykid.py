#longest-uncommon-subsequence
class Solution:
    def findLUSlength(self,a:str,b:str) -> int:
        if a == b:
            return -1
        else:
            if len(a) <= len(b):
                return len(b)
            else:
                return len(a)
