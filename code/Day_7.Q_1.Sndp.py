from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for c, count in d.items():
            if count == 1:
                return s.find(c)
        return -1