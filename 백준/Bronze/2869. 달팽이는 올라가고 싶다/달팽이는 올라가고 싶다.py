# from sys import stdin;
# input = stdin.readline;

A, B, V = map(int, input().split()); # 낮 올 // 밤 내 // 총 길이

if V < A : 
    print(1);
else:
    if (V-A) % (A-B) == 0 :
        print((V-A) // (A-B) +1)
    else :
        print((V-A) // (A-B) +2)