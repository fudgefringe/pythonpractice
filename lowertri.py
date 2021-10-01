def lowertri(x):
  for i in range(len(x)):
    for j in range(len(x)):
      if i<j:
        x[i][j]=0
  return x

  
n=int(input())
l=[]
for i in range(n):
  l1=list(map(int,input().split()))
  l.append(l1)
print(l)

z=lowertri(l)
for i in z:
  print(i)