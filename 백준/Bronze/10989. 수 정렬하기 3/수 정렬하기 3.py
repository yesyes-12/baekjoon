import sys
n = int(sys.stdin.readline())
arr = [0] * 10001 # 0~10000까지의 숫자가 들어올 수 있으므로 10001개의 배열을 만들어준다.
for i in range(n): # 입력받은 숫자를 인덱스로 하여 해당 인덱스의 값을 1씩 증가시킨다.
    arr[int(sys.stdin.readline())] += 1

for i in range(10001): # 0~10000까지의 배열을 순회하며 해당 인덱스의 값이 0이 아니면 그 인덱스를 출력한다.
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)