class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        s1=[]
        for i in words:
            for j in i.split(separator):
                if j:
                    s1.append(j)
        return s1
        