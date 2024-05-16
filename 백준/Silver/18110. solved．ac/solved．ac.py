import sys
input = sys.stdin.readline

def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x)+1
    else:
        return int(x)

N = int(input())
scores = []
for n in range(N):
        scores.append(int(input()))

if N <= 0:
    print(0)
else:
    ignore = roundUp(N*0.15)

    scores.sort()
    print(roundUp(sum(scores[ignore:N-ignore])/(N-(ignore*2))))