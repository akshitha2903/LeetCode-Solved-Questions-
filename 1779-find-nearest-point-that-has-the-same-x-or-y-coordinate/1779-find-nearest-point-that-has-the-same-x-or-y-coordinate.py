class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minDist = math.inf
        ans = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y: 
                if (abs(points[i][0]-x)+abs(points[i][1]-y))<minDist:
                    minDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                    ans = i
        return ans