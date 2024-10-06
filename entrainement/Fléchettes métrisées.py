from typing import List


def flechettes_metrisees(n: int, m: List[int]) -> None:
    best = max(m)
    bestpos = (1, m.index(best))

    before = [0 for i in range(n)]

    
    for i in range(1, n//2+(n+1)%2):
        for a in range(n):
            if a+i<n:
                before[a] += m[a+i]
            if a-i>=0:
                before[a] += m[a-i]

            if before[a] > best:
                best = before[a]
                bestpos = (2*i+1,a)
    print(bestpos[0], bestpos[1])
if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    flechettes_metrisees(n, m)
