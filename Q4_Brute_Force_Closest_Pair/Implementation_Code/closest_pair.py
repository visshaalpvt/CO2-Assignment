import math,time,random,csv
def closest_pair(points):
 if len(points)<2:raise ValueError("need at least two points")
 best=float("inf");pair=None;count=0
 for i in range(len(points)-1):
  for j in range(i+1,len(points)):
   count+=1;d=math.dist(points[i],points[j])
   if d<best:best=d;pair=(points[i],points[j])
 return pair,best,count,count
if __name__=="__main__":
 rng=random.Random(42)
 for n in (100,500,1000,2000):
  pts=[(rng.random()*10000,rng.random()*10000) for _ in range(n)]
  t=time.perf_counter();pair,d,pairs,dist=closest_pair(pts);elapsed=time.perf_counter()-t
  print(n,"unique pairs",pairs,"distance calculations",dist,"seconds",round(elapsed,6),"distance",round(d,4))
