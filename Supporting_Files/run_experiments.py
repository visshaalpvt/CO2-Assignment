import sys,time,random,csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.extend([str(R/"Q1_Sorting_Algorithms/Implementation_Code"),str(R/"Q4_Brute_Force_Closest_Pair/Implementation_Code"),str(R/"Q6_Exhaustive_Search/Implementation_Code")])
from sorting import selection_sort,bubble_sort,insertion_sort
from closest_pair import closest_pair
from exhaustive_knapsack import exhaustive_knapsack
rows=[];rng=random.Random(42)
for n in [100,500,1000]:
 pts=[(rng.random()*10000,rng.random()*10000) for _ in range(n)]
 t=time.perf_counter();res=closest_pair(pts);elapsed=time.perf_counter()-t
 rows.append(["closest_pair",n,round(elapsed,6),res[2]])
for n in [4,8,12,16,18]:
 p=[{"id":str(i),"weight":(i%5)+1,"value":(i%9)+2} for i in range(n)]
 t=time.perf_counter();res=exhaustive_knapsack(p,10);elapsed=time.perf_counter()-t
 rows.append(["exhaustive_knapsack",n,round(elapsed,6),res["examined"]])
out=R/"Supporting_Files/results/experiment_results.csv";out.parent.mkdir(exist_ok=True)
with out.open("w",newline="") as f:
 w=csv.writer(f);w.writerow(["algorithm","n","seconds","primary_operation_count"]);w.writerows(rows)
print(out.read_text())
