class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()

        if len(pattern)!=len(s):
            return False
        
        p={}
        s1={}

        for c,w in zip(pattern,s):
            if c in p and p[c]!=w:
                return False
            if w in s1 and s1[w]!=c:
                return False
            p[c]=w
            s1[w]=c
        return True

        
