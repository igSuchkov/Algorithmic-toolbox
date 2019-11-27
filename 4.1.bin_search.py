# python3
def bin_search(n, mas, index):
    if len(mas) == 1 and n != mas[0]:
        return -1
    half = len(mas) // 2
    if n > mas[half]:
        index += half
        return bin_search(n, mas[half:], index)
    elif n < mas[half]:
        return bin_search(n, mas[:half], index)
    elif n == mas[half]:
        return index + half


items = [int(i) for i in input().split()[1:]]
search_items = [int(i) for i in input().split()[1:]]
res = []
for n in search_items:
    res.append(bin_search(n, items, 0))
print(' '.join(str(i) for i in res))

