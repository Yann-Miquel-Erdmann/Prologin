def reverse_insort(a, x, lo=0, hi=None):

    hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if get(x) > get(a[mid]): hi = mid
        else: lo = mid+1
    a.insert(lo, x)

from typing import List

get = lambda x: teams[x[1]][x[0]]

def compatibilite_heroique(n: int, m: int, teams: List[List[int]]) -> None:
    liste = list(map(lambda x: (0,x[0]),enumerate(teams)))
    liste.sort(reverse=True ,key=lambda x: get(x))
    min_interval =get(liste[0])-get(liste[-1])
    intervals = [(get(liste[-1]),get(liste[0]))]
    for i in range((n-1)*m):
        
        disp = liste.pop()
        if disp[0] == m-1:
            print("\n".join([f"{x[0]} {x[1]}" for x in intervals]))

            return
        reverse_insort(liste, (disp[0]+1,disp[1]))

        interval =get(liste[0])-get(liste[-1])
        if interval < min_interval:
            min_interval = interval

            intervals = [(get(liste[-1]),get(liste[0]))]
        elif interval == min_interval:
            intervals.append((get(liste[-1]),get(liste[0])))

    print("\n".join([f"{x[0]} {x[1]}" for x in intervals]))
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    teams = [list(map(int, input().split())) for _ in range(n)]

    # n = 500
    # m = 500
    # teams = [[i  for i in range(m)] for a in range(n//m)]
    # print(teams)
    compatibilite_heroique(n, m, teams)
