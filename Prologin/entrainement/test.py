def bisect(a,x,lo=0):
    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo


lst = [1,1,1,1]
print( bisect(lst, 1))