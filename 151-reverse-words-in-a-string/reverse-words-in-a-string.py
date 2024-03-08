class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.strip()
        s1=s1.split()
        rs=[]
        for i in range(len(s1)-1,-1,-1):
            rs.append(s1[i])
        return " ".join(rs)
        