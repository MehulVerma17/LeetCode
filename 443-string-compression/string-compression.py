class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        i=0
        while i<len(chars):
            j=i
            while j<len(chars) and chars[i]==chars[j]:
                j+=1

            num=j-i
            chars[index]=chars[i]
            index+=1
            if num>1:
                for k in str(num):
                    chars[index]=k
                    index+=1
            i=j
        chars=chars[:index]
        return len(chars)