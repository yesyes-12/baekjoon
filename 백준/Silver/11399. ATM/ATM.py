import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    times = list(map(int,input_data[1:1+n]))

    times.sort()

    ttime = 0
    current_wait = 0
    for t in times:
        current_wait += t
        ttime += current_wait
        
    print(ttime)


if __name__ == '__main__':
    solve()