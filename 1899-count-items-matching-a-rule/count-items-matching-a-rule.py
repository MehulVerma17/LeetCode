class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0

        for i in items:
            if ruleKey == 'type':
                x = i[0]
            elif ruleKey == 'color':
                x = i[1]
            elif ruleKey == 'name':
                x = i[2]
            if ruleValue == x:
                count += 1
        return count