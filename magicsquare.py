def printms(l):
  for i in range(len(l)):
    for j in range(len(l)):
      print(l[i][j],end=' ')
      # print(i,end='')
      # print(j,end='')
      # print(" ",end=' ')
    print()

def magic_square(n): 
  ms=[[0 for x in range(n)] for y in range(n)]
  i=n//2
  j=n-1
  #this will initilize 1
  num=n*n
  count = 1 #will incerement when we add elements
  while(count<=num):
    if (i==-1 and j==n): #condition 4 done
      i=0
      j=n-2
    else: #condition 2 done
      if j==n: #column exceeds 
        j=0
      if i<0: #row limits
        i=n-1
    if(ms[i][j]!=0):
      i=i+1
      j=j-2
      # print("...i", i)
      # print("...j", j)
      # printms(l)
      #have to skip updating the value
      continue
    else:  
      ms[i][j]=count
      count+=1
    # printms(ms)
    
    i=i-1
    j=j+1
    #condition for next elements
    # print(count)
  return ms


n=int(input("enter n :"))
x=magic_square(n)
printms(x)






