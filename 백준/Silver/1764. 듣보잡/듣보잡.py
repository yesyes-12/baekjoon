import sys
N, M = map(int, sys.stdin.readline().split(" "))

dontListen = []
dontSee = []
for i in range(N):
    name = sys.stdin.readline().rstrip()
    dontListen.append(name)

for i in range(M):
    name = sys.stdin.readline().rstrip()
    dontSee.append(name)

intersect = sorted(set(dontListen) & set(dontSee))
print(len(intersect))
for name in intersect:
    print(name)