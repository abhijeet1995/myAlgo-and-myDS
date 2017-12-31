a=110
while a!=1:
  if a%3==0:
    a/=3
  elif a%5==0:
    a/=5
  elif a%7==0:
    a/=7
  else:
    flag=1
    break
if flag==1:
  print('No')
