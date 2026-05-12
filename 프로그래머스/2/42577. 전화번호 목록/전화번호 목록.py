def solution(phone_book):
    com = {}
    for i in phone_book:
        com[i] = 1
    for i in phone_book:
        # print(i)
        temp = ""
        for j in i[:-1]:
            temp += j
            # print(temp)
            if temp in com:
                return False
    return True
   
        