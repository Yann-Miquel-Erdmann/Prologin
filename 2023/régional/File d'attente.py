
from typing import List


def attente_minimale(n: int, charges: List[int]) -> None:
    """
    :param n: le nombre de clients
    :param charges: la liste des poids du matériel de chaque soldat, en kilogrammes
    """
    charges.sort()
    temps_total = 0
    temps = 0
    for e in charges:
        temps_total+=temps
        temps+=e
    print(temps_total)

if __name__ == "__main__":
    n = int(input())
    charges = list(map(int, input().split()))
    attente_minimale(n, charges)
