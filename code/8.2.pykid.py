def patfind(word):
    ls = []
    already = {}
    i=0
    final=''
    for alpha in word:
        if alpha in word:
            already[alpha]=str(i)
            i+=1
        final += already[alpha]
    return final

class Solution:
    def findAndReplacePattern(self,words:List[str],pattern:str) -> List[str]:
        result = []
        patt=patfind(pattern)
        for word in words:
            newpatt=patfind(word)
            if newpatt==patt:
                result.append(word)
        return result
