class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map={}
        for i in paths:
            map[i[0]]=i[1]
        for j in paths:
            if j[1] not in map:
                return j[1]
        return ""