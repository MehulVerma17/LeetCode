class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

        '''
        d1=dict(Counter(s))
        d2=dict(Counter(t))

        if len(d1)!=len(d2):
            return False

        for i,j in zip(d1,d2):
            if d1[i]!=d2[j]:
                return False
        return True
        '''

