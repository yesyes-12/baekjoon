#2588
a = int(input())
b = int(input())
r3 = a*(b%10)
r4 = a*((b%100)-(b%10))/10
r5 = a*(b-(b%100))/100
r6 = a*b
print(r3,int(r4),int(r5),r6, sep='\n')