
from typing import List
from bisect import i

def sabotage(n: int, m: int, beaute: List[int], etage: List[int]) -> None:
    profondeurs = [0 for i in range(n)]
    fils = [[]for i in range(n)]
    somme = [beaute[0]]
    for i,elem in enumerate(etage):
        profondeurs[i] = profondeurs[elem-1] +1
        fils[i] = []

        if i !=0:
            somme.append(somme[elem-1] + beaute[i])
            fils[elem-1].append(i)

    
    bombes = 0
    r = list(filter(lambda x: len(fils[x]) == 0, list(range(n))))
    # print(r)
    for i in r[::-1]:

        if profondeurs[i] < bombes:
            continue

        count = profondeurs[i]-1

        start = i
        for a in range(profondeurs[i]-bombes):

            indice = start
            while somme[i] - somme[start] + somme[indice] > m:
                if indice == 0:
                    indice = -1
                    break

                indice = etage[indice]-1
                
            if indice != -1 and somme[i] - somme[start] + somme[indice] <= m:
                
                if profondeurs[start] - profondeurs[indice] < count:
                    
                    count =profondeurs[start] - profondeurs[indice]
            
            start = etage[start]-1



        if count>bombes:
            bombes = count

        start = etage[start]-1

    # print(fils)
    # print(somme)
    # print(profondeurs)
    print(bombes)

    """
    :param n: le nombre de parties du monument
    :param m: la beauté maximale
    :param beauté: les beautés de chaque partie
    :param étage: une indication de la partie vers laquelle on est dirigés en empruntant les escaliers, pour chaque partie. Il est garanti que la première valeur correspondant au sommet est 1, vous pouvez ignorer cette valeur puisque le sommet n'a pas d'escaliers

    """
    # TODO Afficher le nombre minimal de kits tel qu'il soit possible de
    # réaliser un sabotage entraînant une beauté n’excédant pas **M**.
    pass


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    beaute = list(map(int, input().split()))
    etage = list(map(int, input().split()))
    sabotage(n, m, beaute, etage)
