class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2==str2+str1:
            gcd=math.gcd(len(str1),len(str2))
            s1=str1[0:gcd]
            return s1
        return ""
       