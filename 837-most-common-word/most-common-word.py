class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        r="!?',;."

        s=s.lower()

        for char in r:
            s=s.replace(char,' ')

        c=Counter(s.split())

        most_common=""
        max_frequency=0

        for i,j in c.items():
            if i not in banned and j>max_frequency:
                most_common=i
                max_frequency=j
        return most_common

        