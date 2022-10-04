double average(int* salary, int salarySize){
int max,min,i,sum;
    sum=max=min=salary[0];
    for(i=1;i<salarySize;i++){
        if(max<salary[i])
            max=salary[i];
        if(min>salary[i])
            min=salary[i];
        sum+=salary[i];
    }
    return (sum-min-max)/(salarySize-2.0);    
}