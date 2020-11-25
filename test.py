a=int(input())
b=int(input())
if a<b:
  for i in range(1,10):
    print(i)
else:
  for i in range(b+1,a,-1):
    print(i)
