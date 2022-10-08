int nearestValidPoint(int x, int y, int** points, int pointsSize, int* pointsColSize){
int index=-1,min=INT_MAX;
for(int i=pointsSize-1;i>=0;i--)
if ((points[i][0]==x)||(points[i][1]==y))
    if (abs(x-points[i][0])+abs(y-points[i][1])<= min){
                min = abs(points[i][0] - x) + abs(points[i][1] - y);
                index=i;
    }
return index;
}