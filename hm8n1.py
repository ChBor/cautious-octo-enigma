def buble_sort(l):
    t = l.copy()
    for n in range(len(t)):
        for i in range(len(t) - n):
#Мы прохожим по элементам списка и берем следующий элемент, а поскольку у последнего элемента нет срседа справа, нужно отнять один
            if t[i]>t[n]:
                t[i], t[n] = t[n], t[i]
    return t
nums = [4, 1, 6, 3, 2, 7, 8, -3]
sorted = buble_sort(nums)
print("Original:", sorted)

def buble_sort(l):
    t = l.copy()
    for n in range(len(t)):
        for i in range(len(t) - 1):
            if t[i]>t[n]:
                t[i], t[n] = t[n], t[i]
    return t
nums = [4, 1, 6, 3, 2, 7, 8, -3]
sorted = buble_sort(nums)
print("Correct version:", sorted, "\n")










