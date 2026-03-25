def solution(phone_number):
    if len(phone_number)==4:
        return phone_number
    answer = phone_number[-4:]
    s = "*" * len(phone_number[:-4])
    
    return s+answer