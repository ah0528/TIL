def search_num(a, x):
    n =len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
            break

    return -1

print(search_num([2,5,7,2,5,6,9], 5 ))