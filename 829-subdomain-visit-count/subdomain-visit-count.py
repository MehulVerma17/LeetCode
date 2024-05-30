class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d1=defaultdict(int)

        for i in cpdomains:
            count, domain = i.split(" ")
            count = int(count)

            sub=domain.split(".")
            for j in range(len(sub)):
                sub1=".".join(sub[j:])
                d1[sub1] +=count

        result = [str(count)+" "+sub1 for sub1,count in d1.items()]
        return result