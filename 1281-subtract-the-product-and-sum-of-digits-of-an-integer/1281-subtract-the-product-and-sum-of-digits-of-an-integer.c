int subtractProductAndSum(int n){
int pr=1,sum=0,ans=0;
    while(n!=0){
    pr*=n%10;
    sum+=n%10;
    n=n/10;
    }
    ans=pr-sum;
    return ans;
}