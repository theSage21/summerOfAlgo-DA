class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if [word.index(i) for i in word] == [pattern.index(ptr) for ptr in pattern]]
        