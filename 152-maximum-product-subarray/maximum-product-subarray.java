class Solution {
    public int maxProduct(int[] a) {
        int max=a[0],m=a[0],min=a[0],temp=0;
        for(int i=1;i<a.length;i++)
        {       
            if(a[i]>0)
            {
                max=Math.max(a[i],max*a[i]);
                min=Math.min(a[i],min*a[i]);
            }
            else if(a[i]==0)
            max=min=0;
            else
            {
                temp=max;
                max=Math.max(a[i],min*a[i]);
                min=Math.min(a[i],temp*a[i]);
            }
            m=Math.max(m,max);
        }
        return m;
        }
}