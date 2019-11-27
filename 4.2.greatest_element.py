# python3
def greatest_element(c, mas):
    m = c//2
    d, res = dict(), 0
    for el in mas:
        if el in d.keys():
            d[el] += 1
        else:
            d[el] = 1
    for k, v in d.items():
        if v > m:
            res += 1
    return res


n = int(input())
lst = map(int, input().split())
print(greatest_element(n, lst))
