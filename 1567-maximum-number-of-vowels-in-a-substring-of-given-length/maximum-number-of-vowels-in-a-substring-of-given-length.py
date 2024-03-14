class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=('aeiou')
        startindex=0
        endindex=k
        c=0
        for i in range(k):
            if s[i] in vowels:
                c+=1
        maxc=c

        if c==k:
            return c
        
        while endindex<len(s):
            if s[startindex] in vowels:
                c-=1
            startindex+=1

            if s[endindex] in vowels:
                c+=1
            endindex+=1

            maxc=max(maxc,c)
        return maxc

        '''
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
        '''