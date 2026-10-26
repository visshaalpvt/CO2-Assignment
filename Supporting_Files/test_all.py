import sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for q in ["Q1_Sorting_Algorithms","Q2_Sequential_Search","Q3_Brute_Force_String_Matching","Q4_Brute_Force_Closest_Pair","Q5_Brute_Force_Convex_Hull","Q6_Exhaustive_Search"]:
 sys.path.insert(0,str(next((R/q/"Implementation_Code").glob("*.py")).parent))
from sorting import selection_sort,bubble_sort,insertion_sort
from sequential_search import sequential_search
from string_matching import brute_force_match
from closest_pair import closest_pair
from convex_hull import brute_force_hull
from exhaustive_knapsack import exhaustive_knapsack
assert all(fn([4,1,3,2])[0]==[1,2,3,4] for fn in (selection_sort,bubble_sort,insertion_sort))
assert sequential_search([{"tool_id":"a"},{"tool_id":"b"}],"b")[0]==1
assert brute_force_match("ababa","aba")[0]==[0,2]
pts=[(0,0),(1,0),(4,0),(0,3)]
assert closest_pair(pts)[2]==6
h=brute_force_hull([(0,0),(4,0),(4,4),(0,4),(2,2)])
assert set(h)=={(0,0),(4,0),(4,4),(0,4)}
r=exhaustive_knapsack([{"id":"A","weight":2,"value":6},{"id":"B","weight":3,"value":10},{"id":"C","weight":4,"value":12}],5)
assert r["value"]==16
print("PASS Q1 sorting algorithms")
print("PASS Q2 sequential search")
print("PASS Q3 brute-force string matching")
print("PASS Q4 brute-force closest pair")
print("PASS Q5 brute-force convex hull")
print("PASS Q6 exhaustive knapsack")
print("Q7 requires measured evidence and must be completed after Q1-Q6 experiments.")
