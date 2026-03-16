def FizzBuzz():
    strings = [ input().strip() for _ in range(3)]

    n = 0
    for i in range(3):
        if strings[i].isdigit():
            n = int(strings[i]) + (3-i)
            break

    if (n % 3 == 0) and (n % 5 ==0):
        print("FizzBuzz")
    elif (n % 3 == 0) and not (n % 5 == 0):
        print("Fizz")
    elif not (n % 3 == 0) and (n % 5 ==0):
        print("Buzz")
    else:
        print(n)
FizzBuzz()