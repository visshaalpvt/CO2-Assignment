import math
def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
def brute_force_hull(points):
 pts=sorted(set(tuple(p) for p in points))
 if len(pts)<=1:return pts
 if all(cross(pts[0],pts[-1],p)==0 for p in pts):return [pts[0],pts[-1]] if len(pts)>1 else pts
 hull=set()
 n=len(pts)
 for i in range(n):
  for j in range(i+1,n):
   pos=neg=False
   for k in range(n):
    if k in (i,j):continue
    s=cross(pts[i],pts[j],pts[k])
    if s>0:pos=True
    elif s<0:neg=True
   if not(pos and neg):hull.add(pts[i]);hull.add(pts[j])
 cx=sum(p[0] for p in hull)/len(hull);cy=sum(p[1] for p in hull)/len(hull)
 return sorted(hull,key=lambda p:math.atan2(p[1]-cy,p[0]-cx))
if __name__=="__main__":
 tests=[[(0,0),(4,0),(4,4),(0,4),(2,2),(1,1)],[(0,0),(1,1),(2,2),(3,3),(1,2),(2,1)]]
 for p in tests:print("points",p,"hull",brute_force_hull(p))
