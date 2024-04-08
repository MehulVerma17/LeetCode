class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1=dict(Counter(magazine))
        
        for i in ransomNote:
            if i in d1 and d1[i]>0:
                d1[i]-=1
            else:
                return False
        return True
        

