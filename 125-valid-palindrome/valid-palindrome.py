class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=s.lower()
        l=[]
        
        for i in lower:
            if i.isalpha() or i.isdigit():
                l.append(i)
        l="".join(l)

        if l[::-1]==l:
            return True
        else:
            return False