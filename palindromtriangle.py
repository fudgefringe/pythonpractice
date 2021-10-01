n=int(input())
k=1
for i in range(1,n+1):
  for j in range(1,2*i):
    x=(2*i-1)//2+1
    if(j<=x):
      print(j,end='')
      y=x
    else:
      y-=1
      print(y,end='')
  print()