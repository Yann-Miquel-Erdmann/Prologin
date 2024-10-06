from typing import List


def ordre(k: int, n: int, tailles: List[int]) -> None:
    """
    :param k: le nombre magique
    :param n: le nombre de personnes
    :param tailles: la liste des tailles de chaque personne
    """
    # TODO Afficher **OUI** s'il est possible de trier les personnes par taille
    # ou **NON** si ce n'est pas possible.
    liste = sorted(tailles)
    

    for i in range(k):
        counters = [0 for i in range(1000)]
        for j in range(i,n,k):
            counters[liste[j]-1] +=1
        
        for j in range(i,n,k):
            if counters[tailles[j]-1] != 0:

                counters[tailles[j]-1] -=1
            else:
                print("NON")
                return
    print("OUI")

if __name__ == "__main__":
    k = int(input())
    n = int(input())
    tailles = list(map(int, input().split()))
    ordre(k, n, tailles)
