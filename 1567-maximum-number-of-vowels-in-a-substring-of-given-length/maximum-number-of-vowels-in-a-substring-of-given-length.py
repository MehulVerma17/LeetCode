class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=('aeiou')
        startindex=0
        endindex=0
        c=0
        res=0
        while endindex<len(s) and startindex<len(s):
            if s[endindex] in vowels:
                c+=1
            if endindex-startindex+1>k:
                if s[startindex] in vowels:
                    c-=1 
                startindex+=1
            res=max(res,c)
            endindex+=1
        return res