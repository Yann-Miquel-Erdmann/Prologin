
from dataclasses import dataclass
from typing import List


@dataclass
class Mutation:
    """une mutation d'une rotation"""

    position: int  # la position de la rotation qui mute
    type: str  # la nouvelle rotation à effectuer


def resultats_rotations(
    n: int, m: int, rotations: List[str], q: int, mutations: List[Mutation]
) -> None:
    """
    :param n: la quantité de nombres à positionner sur le cercle
    :param m: le nombre de rotations
    :param rotations: la liste des rotations initiales
    :param q: le nombre de mutations
    :param mutations: la liste des mutations à effectuer et évaluer
    """
    g = 0
    s = False
    for e in rotations:
        if e == "S":
            s = not s
        elif e == "G": 
            g+=1
        else:
            g-=1
    for i in range(q):
        if rotations[mutations[i].position-1] == "S":
            s = not s
        elif rotations[mutations[i].position-1] == "G":
            g -= 1
        else:
            g += 1
            
        rotations[mutations[i].position-1] = mutations[i].type
        
        if rotations[mutations[i].position-1] == "S":
            s = not s
        elif rotations[mutations[i].position-1] == "G":
            g += 1
        else:
            g -= 1


        print(" ".join(map(str, [int(a+g+(n/2)*int(s))%n+1 for a in range(0,n)])))


    



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    rotations = list(input())
    q = int(input())
    mutations = [
        Mutation(*map(lambda f, x: f(x), (int, str), input().split()))
        for _ in range(q)
    ]
    resultats_rotations(n, m, rotations, q, mutations)
