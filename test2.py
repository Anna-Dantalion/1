a=int(input())
b=int(input())
for i in range(a,b+1):
  f=i//100
  d=((i%100)%10)*10+(i%100)//10
  if f==d:
    print(i)
