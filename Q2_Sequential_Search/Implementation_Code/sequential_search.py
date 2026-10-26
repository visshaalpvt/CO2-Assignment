def sequential_search(records,target):
 comparisons=0
 for i,record in enumerate(records):
  comparisons+=1
  if record["tool_id"]==target:return i,comparisons
 return -1,comparisons
if __name__=="__main__":
 records=[{"tool_id":"T-101","technician":"TECH-1"},{"tool_id":"T-184","technician":"TECH-7"},{"tool_id":"T-220","technician":"TECH-3"}]
 for q in ["T-101","T-220","T-999"]:
  i,c=sequential_search(records,q)
  print(q, "index",i,"comparisons",c,"record",records[i] if i>=0 else None)
