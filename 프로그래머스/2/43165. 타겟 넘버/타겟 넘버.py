
def solution(numbers, target):
    cases = [0]
    
    for num in numbers:
        temp = []
        print(num)
        for case in cases:
            # 이번 숫자를 더한 값과 뺀 값을 배열에 추가
            temp.append(case + num)
            #print(f"+:{case+num}")
            temp.append(case - num)
            #print(f"-:{case-num}")
        #print(temp)
        cases = temp
    
    return cases.count(target)