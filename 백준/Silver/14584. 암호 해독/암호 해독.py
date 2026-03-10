import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    cipher = input_data[0]
    n = int(input_data[1])
    dictionary = input_data[2:2+n]
    
    # 0칸부터 25칸까지 모든 경우의 수를 다 밀어보기 (완전탐색)
    for shift in range(26):
        decrypted_chars = []
        
        for char in cipher:
            # 1. 문자를 0~25 사이의 숫자로 바꿈: ord(char) - ord('a')
            # 2. shift 만큼 더하고 26으로 나눈 나머지를 구함 (z를 넘어가면 다시 a로 돌아오게 함)
            # 3. 다시 아스키코드 값으로 복원: + ord('a')
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            decrypted_chars.append(new_char)
            
        # 리스트에 담긴 문자들을 하나의 문자열로 합치기
        decrypted_str = "".join(decrypted_chars)
        
        # 해독된 문자열 안에 사전의 단어가 하나라도 포함되어 있는지 검사
        for word in dictionary:
            if word in decrypted_str:
                print(decrypted_str)
                return  # 답을 찾았으므로 프로그램 즉시 종료

if __name__ == '__main__':
    solve()