import random
class NQueensCSP:
 def __init__(self,N):
   self.N=N
   self.domains=list(range(N))
 def conflicts(self,assignment):
  count=0
  for i in range(self.N):
   for j in range (i+1,self.N):
    if assignment[i]==assignment[j] or abs(assignment[i]-assignment[j])==j-i:
     count+=1
  return count
 def min_conflicts(selfs,max_steps=1000):
  assignment=[ramdom.choice(self.domains)for_in ranges(self.N)]
  for_in range(max_steps):
   if self.conflicts(assignment)==0:
    return assignment
   conflicts_vars=[i for i in range(self.N)if self.conflicts(assignment)>0]
   var=random.choice(conflictd_vars)
   min_conflict_value=min(self.domains,key=lambda val:self.conflicts(assignment[:var]+[val]+assignment[var+1:]))
   assignment[var]=min_conflict_value
  return None
N=8
nqueens=NQueensCSP(N)
solution=nqueens.min_conflicts()
if solution:
    print("solution found:",solution)
else:
    print("no solution found within the maximum number of steps")
