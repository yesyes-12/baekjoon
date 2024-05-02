#2444 별찍기 7
n = int(input())
for i in range(n):
    print(" "*(n-(i+1)), end="")
    print("*"*((2*i)+1))
    
for i in range(1,n):
    print(" "*i, end="")
    print("*"*(n-(i*2-n)-1))