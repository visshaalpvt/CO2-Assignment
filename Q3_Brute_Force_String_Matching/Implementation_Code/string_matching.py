def brute_force_match(text,pattern):
 if pattern=="": return list(range(len(text)+1)),0
 n,m=len(text),len(pattern);positions=[];comparisons=0
 for s in range(n-m+1):
  j=0
  while j<m:
   comparisons+=1
   if text[s+j]!=pattern[j]:break
   j+=1
  if j==m:positions.append(s)
 return positions,comparisons
if __name__=="__main__":
 cases=[("security event found","event","quick mismatch / match"),("A"*30+"B","A"*9+"B","repeated-prefix high work"),("abcabcabc","abc","overlapping matches")]
 for t,p,label in cases:print(label, "positions/count",brute_force_match(t,p))
