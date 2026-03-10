import sys

def is_subsequence(s, t):
    # i는 s의 위치를 가리키고, j는 t의 위치를 가리킵니다.
    i = 0
    j = 0
    
    # 두 포인터 중 하나라도 문자열 끝에 도달하면 탐색을 종료합니다.
    while i < len(s) and j < len(t):
        # 두 문자가 같다면 s의 다음 문자를 찾기 위해 i를 한 칸 이동합니다.
        if s[i] == t[j]:
            i += 1
            
        # t의 포인터 j는 문자가 같든 다르든 무조건 1씩 증가하며 앞으로 전진합니다.
        j += 1
        
    # i가 s의 길이와 같아졌다면, s의 모든 문자를 t에서 순서대로 다 찾았다는 의미입니다.
    if i == len(s):
        return "Yes"
    else:
        return "No"

while True:
    try:
        s, t = sys.stdin.readline().rstrip().split(" ")
        print(is_subsequence(s,t))
    except:
        break