def exhaustive_knapsack(packages,capacity):
 best_value=0;best=[];feasible_count=0;examined=0
 n=len(packages)
 for mask in range(1<<n):
  examined+=1;weight=value=0;subset=[]
  for i,p in enumerate(packages):
   if mask>>i&1:weight+=p["weight"];value+=p["value"];subset.append(p["id"])
  if weight<=capacity:
   feasible_count+=1
   if value>best_value:best_value=value;best=subset
 return {"subset":best,"value":best_value,"examined":examined,"feasible":feasible_count}
if __name__=="__main__":
 packages=[{"id":"A","weight":2,"value":6},{"id":"B","weight":3,"value":10},{"id":"C","weight":4,"value":12},{"id":"D","weight":5,"value":15}]
 for n in (4,8,12,16):
  data=(packages*4)[:n]
  print("n",n,"result",exhaustive_knapsack(data,10))
