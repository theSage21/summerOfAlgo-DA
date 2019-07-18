class Solution:
    def firstUniqChar(self,s:str) -> int:
        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] > 1:
                continue
            return i
        return -1
