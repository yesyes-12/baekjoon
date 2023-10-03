num_list = [i for i in range(1, 31)]
for i in range(28):
    n = int(input())
    num_list.remove(n)
print(min(num_list))
print(max(num_list))