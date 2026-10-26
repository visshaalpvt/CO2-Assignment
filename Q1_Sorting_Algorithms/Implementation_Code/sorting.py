import time
def selection_sort(data):
 a=list(data); comps=swaps=0
 for i in range(len(a)-1):
  m=i
  for j in range(i+1,len(a)):
   comps+=1
   if a[j]<a[m]:m=j
  if m!=i:a[i],a[m]=a[m],a[i];swaps+=1
 return a,{"comparisons":comps,"swaps":swaps}
def bubble_sort(data):
 a=list(data);comps=swaps=0
 for end in range(len(a)-1,0,-1):
  changed=False
  for j in range(end):
   comps+=1
   if a[j]>a[j+1]:a[j],a[j+1]=a[j+1],a[j];swaps+=1;changed=True
  if not changed:break
 return a,{"comparisons":comps,"swaps":swaps}
def insertion_sort(data):
 a=list(data);comps=shifts=0
 for i in range(1,len(a)):
  key=a[i];j=i-1
  while j>=0:
   comps+=1
   if a[j]>key:a[j+1]=a[j];shifts+=1;j-=1
   else:break
  a[j+1]=key
 return a,{"comparisons":comps,"shifts":shifts}
if __name__=="__main__":
 cases={"nearly_sorted":[1,2,3,5,4,6,7,8],"reverse":[8,7,6,5,4,3,2,1],"duplicates":[3,1,3,2,1,2]}
 for name,data in cases.items():
  print("\n",name,data)
  for fn in (selection_sort,bubble_sort,insertion_sort):
   start=time.perf_counter();out,stats=fn(data);elapsed=time.perf_counter()-start
   print(fn.__name__,out,stats,"seconds",round(elapsed,8))
