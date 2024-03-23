class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d1=dict(Counter(s))
        d2=dict(Counter(t))

        for i in d1:
            if i not in d2:
                return False
            elif d1[i] != d2[i]:
                return False
        return True
