class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        c=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        if c==len(s):
            return True
        else:
            return False

            