a, b, c = 0, 0, 0
T = int(input())
if T%10!=0:
  print(-1)
elif T//300>0:
  a = T//300
  T = T - a*300
  b = T//60
  if b>0:
    T = T - b*60
    c = T//10
  elif b<=0:
    c = T//10
  print(a, b, c)
elif T//300<=0:
  b = T//60
  if b>0:
    T = T - b*60
    c = T//10
  elif b<=0:
    c = T//10
  print(a, b, c)