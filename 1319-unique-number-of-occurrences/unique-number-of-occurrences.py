class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        if len(Counter(arr))==len(set(Counter(arr).values())):
            return True 
        else:
            return False
        '''
        #less optimal
        occur=0
        d={}
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    occur+=1
            d[arr[i]]=occur
            occur=0
        if len(d)==len(set(d.values())):
            return True
        else:
            return False
        '''