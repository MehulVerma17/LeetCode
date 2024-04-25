class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        l=[]
        for i in range(len(s)):
            l.append(s[i][::-1])
        return " ".join(l)