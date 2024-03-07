class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels=("aeiouAEIOU")
        low=0
        high=len(s)-1
        temp=""
        while low<high:
            if s[low] not in vowels:
                low+=1
            elif s[high] not in vowels:
                high-=1
            else:
                temp=s[low]
                s[low]=s[high]
                s[high]=temp
                low+=1
                high-=1
        return "".join(s)


        
