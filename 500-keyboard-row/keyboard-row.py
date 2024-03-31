class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1="qwertyuiop"
        r2="asdfghjkl"
        r3="zxcvbnm"
        l=[]

        for i in words:
            w=i.lower()
            if len(set(r1+w))==len(r1) or len(set(r2+w))==len(r2) or len(set(r3+w))==len(r3) :
                l.append(i)
        return l