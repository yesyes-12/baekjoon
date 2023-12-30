sugar = int(input())

delivery = 0

while sugar >= 0 :
    if sugar % 5 == 0 :
        delivery = delivery + (sugar // 5)
        print(delivery)
        break
    sugar = sugar - 3  
    delivery = delivery + 1
else :
    print(-1)