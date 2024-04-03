class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=[]
        s2=[]
        for i in digits:
            s.append(str(i))
        s1=''.join(s)
        s1=int(s1)
        
        s1+=1

        s1=str(s1)
        for i in s1:
            s2.append(int(i))
        
        return s2