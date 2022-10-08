class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res=sum=0
        pro=1
        while (n!=0):
            pro*=n%10
            sum+=n%10
            n=n//10
        res=pro-sum
        return res
        