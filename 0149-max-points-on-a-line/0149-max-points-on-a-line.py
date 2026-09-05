from math import gcd
class Solution:
    def maxPoints(self, points):
        n=len(points)
        ans=0
        if n<=2:
            return n

        for i in range(n):
            x1=points[i][0]
            y1=points[i][1]
            slopes={}
            for j in range(i+1,n):
                x2=points[j][0]
                y2=points[j][1]

                dy=y2-y1
                dx=x2-x1

                if dx==0:
                    slope=(1,0)
                else:
                    g=gcd(dy,dx)
                    dy//=g
                    dx//=g

                    if dx<0:
                        dx=-dx
                        dy=-dy

                    slope=(dy,dx)
                slopes[slope]=slopes.get(slope,0)+1
            if slopes:
                ans=max(ans,max(slopes.values())+1)
        return ans

        