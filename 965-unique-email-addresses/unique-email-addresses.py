class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            temp=emails[i].split("@")
            x=""
            for j in temp[0]:
                if j=='.':
                    continue
                elif j=='+':
                    break
                else:
                    x+=j
            emails[i]=x+"@"+temp[1]

        return len(set(emails))