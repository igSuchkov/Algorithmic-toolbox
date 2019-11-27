# python3
def partition(mas):
    pivot = mas[0]
    low, equal, high = [], [], []
    for i in mas:
        if i < pivot:
            low.append(i)
        elif i > pivot:
            high.append(i)
        else:
            equal.append(i)
    return low, equal, high


def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    low, pivot, high = partition(mas)
    return quick_sort(low) + pivot + quick_sort(high)


n = int(input())
lst = [int(i) for i in input().split()]
print(' '.join(str(i) for i in quick_sort(lst)))
