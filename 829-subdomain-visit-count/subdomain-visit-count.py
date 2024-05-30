class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for i in cpdomains:
            times, domain = i.split()
            n = domain.count('.')
            for j in range(n+1):
                temp = domain.split('.',j)[-1]
                if temp in dic:
                    dic[temp] += int(times)
                else:
                    dic[temp] = int(times)
        
        res = []
        for i in dic:
            res.append(f"{dic[i]} {i}")
        
        return res