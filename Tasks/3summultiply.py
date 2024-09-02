class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res=0
        c=Counter(arr)
        for i in range(101):
            if c[i]==0:
                continue
            l,r = i,100
            while l<=r:
                if l+r<target-i:
                    l+=1
                elif l+r>target-i:
                    r-=1
                else:
                    if i==l==r:
                        res+=(c[i]*(c[i]-1)*(c[i]-2))//6
                    elif i==l:
                        res+=(c[i]*(c[i]-1)*c[r])//2
                    elif l==r:
                        res+=(c[i]*c[r]*(c[r]-1))//2
                    else:
                        res+=c[i]*c[l]*c[r]
                    l+=1
                    r-=1
        return res%(10**9+7)




