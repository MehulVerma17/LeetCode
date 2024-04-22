class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l1=[]
        l2=[]

        for i in range(len(s)):
            if s[i]==c:
                l1.append(i)
        for i in range(len(s)):
            l3=[]
            for j in l1:
                l3.append(abs(i-j))
            l2.append(min(l3))
        return l2