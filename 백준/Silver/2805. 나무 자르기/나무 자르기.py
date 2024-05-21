n, m = map(int, input().split()) # 나무수 ,원하는길이
trees = list(map(int, input().split()))

trees.sort()
min_h = 0; max_h = max(trees)
while min_h <= max_h:
    sum_rm = 0
    expect = (min_h + max_h) // 2

    for i in range(len(trees)):
        r = trees[i] - expect
        if r > 0:
            sum_rm += r

    if sum_rm == m:
        print(expect)
        break
    elif sum_rm > m:
        min_h = expect
        if max_h - min_h == 1:
            print(expect)
            break
    elif sum_rm < m:
        max_h = expect
