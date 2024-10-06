def reverse_insort(a, x, lo=0, hi=None):

    while lo < hi:
        mid = (lo+hi)//2
        if x[0] > a[mid][0]: hi = mid
        else: lo = mid+1
    a.insert(lo, x)

def bisect(a,x,hi,lo=0):
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid][0]: hi = mid
        else: lo = mid+1
    return lo


nb = int(input())
planetes = list(map(int,input().split(" ")))
# import random
# nb = 1000000
# planetes = [random.randint(1,nb)for i in range(nb,0,-1)]
# print(planetes)
res = [0 for i in range(nb)]

lst = []


top = 1
for i in range(nb-1,-1,-1):
    a = len(lst)
    if a!=0:
        n = bisect(lst, planetes[i],hi=top)
        
        for b in range(n,top):
            res[lst[b][1]] = i+1
        top = n+1
    reverse_insort(lst, (planetes[i],i),hi=top-1)


print(" ".join(map(str,res)))
# print("done")