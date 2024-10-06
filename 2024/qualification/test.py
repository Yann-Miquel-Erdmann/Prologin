import timeit

def fastInsert(liste,elem):
    low = 0
    high = len(liste)
    while high > low :
        mid = (low + high) // 2
        if liste[mid] > elem:
            high = mid
        else:
            low = mid+1
    liste.insert(low,elem)
    return liste

def fastRemove(liste,elem):
    low = 0
    high = len(liste)
    while high > low :
        mid = (low + high) // 2
        if liste[mid] > elem:
            high = mid
        else:
            low = mid+1
    liste.pop(low)
    return liste

def test1(liste,k):
    for i in range(len(liste)-k):
        a = max(liste[i: i+k])

def test2(liste,k):
    sliding_list = sorted(liste[0:k])
    for i in range(len(liste)-k):
        a = sliding_list[-1]
        fastRemove(sliding_list,liste[i])
        fastInsert(sliding_list,liste[i+k])

def test3(liste,k):
    import bisect
    sliding_list = sorted(liste[0:k])
    for i in range(len(liste)-k):
        a = sliding_list[-1]
        sliding_list.pop(bisect.bisect(sliding_list, liste[i]))
        bisect.insort(sliding_list, liste[i+k])



# print(timeit.timeit("test1(liste, 1000)",setup="from __main__ import test1; liste = list(range(100000))", number=10))
# print(timeit.timeit("test2(liste, 10000)",setup="from __main__ import test2, fastInsert,fastRemove; liste = list(range(100000))", number=10))
print(timeit.timeit("test3(liste, 10000)",setup="from __main__ import test3;liste = list(range(100000))", number=10))

