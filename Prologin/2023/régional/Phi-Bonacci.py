
from typing import List


def phibonacci(n: int, x: List[int]) -> None:
    """
    :param n: la taille initiale de la machine
    :param x: la machine à compacter
    """
    mod = 1000_000_007
    x = list(map(lambda e: e%mod, x))

    for i in range(len(x)-1, 1, -1):
        x[i-1]+=x[i]
        x[i-2]+=x[i]
        x[i-1]%=mod
        x[i-2]%=mod

        x.pop()


    print(" ".join(map(str,x)))



if __name__ == "__main__":
    n = int(input())
    x = list(map(int, input().split()))
    phibonacci(n, x)
